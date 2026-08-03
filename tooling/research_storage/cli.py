"""Discover, resolve, and compare Research content replicas."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tomllib
import uuid
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Sequence


RESEARCH_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = RESEARCH_ROOT / "storage" / "storage.toml"


class StorageError(ValueError):
    """A user-facing storage configuration or resolution error."""


def load_toml(path: Path) -> dict[str, Any]:
    try:
        with path.open("rb") as handle:
            return tomllib.load(handle)
    except FileNotFoundError as exc:
        raise StorageError(f"configuration not found: {path}") from exc
    except tomllib.TOMLDecodeError as exc:
        raise StorageError(f"invalid TOML in {path}: {exc}") from exc


def configured_path(config_path: Path, raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute() or ".." in path.parts:
        raise StorageError("configured storage paths must stay inside storage/")
    return (config_path.parent / path).resolve()


def normalize_id(raw: object) -> str:
    try:
        parsed = uuid.UUID(raw)
    except (ValueError, AttributeError) as exc:
        raise StorageError(f"invalid node id: {raw!r}") from exc
    normalized = str(parsed)
    if normalized != raw or parsed.version != 4:
        raise StorageError(f"node id must be a canonical UUIDv4: {raw!r}")
    return normalized


def normalize_path(raw: object) -> str:
    if not isinstance(raw, str):
        raise StorageError(f"invalid rooted path: {raw!r}")
    if not raw or raw != raw.strip() or "\\" in raw or raw.startswith("/"):
        raise StorageError(f"invalid rooted path: {raw!r}")
    if raw.endswith("/") or "//" in raw:
        raise StorageError(f"invalid rooted path: {raw!r}")
    if any(part in {"", ".", ".."} for part in raw.split("/")):
        raise StorageError(f"invalid rooted path: {raw!r}")
    return PurePosixPath(raw).as_posix()


def normalize_selector(
    node_id: str | None, rooted_path: str | None
) -> tuple[str | None, str | None]:
    if node_id is None and rooted_path is None:
        raise StorageError("pass --id, --path, or both")
    return (
        normalize_id(node_id) if node_id is not None else None,
        normalize_path(rooted_path) if rooted_path is not None else None,
    )


def source_spec(config: dict[str, Any], source: str) -> dict[str, Any]:
    spec = config.get("sources", {}).get(source)
    if not isinstance(spec, dict):
        available = ", ".join(sorted(config.get("sources", {})))
        raise StorageError(f"unknown source {source!r}; available: {available}")
    if not isinstance(spec.get("enabled"), bool):
        raise StorageError(f"sources.{source}.enabled must be boolean")
    if spec.get("kind") not in {"directory", "remote"}:
        raise StorageError(f"unsupported source kind for {source!r}")
    if not isinstance(spec.get("routes"), str) or not spec["routes"]:
        raise StorageError(f"sources.{source}.routes must be a path")
    if spec["kind"] == "directory" and (
        not isinstance(spec.get("root"), str) or not spec["root"]
    ):
        raise StorageError(f"sources.{source}.root must be a path")
    return spec


def load_config(path: Path = DEFAULT_CONFIG) -> dict[str, Any]:
    config = load_toml(path)
    if config.get("version") != 1:
        raise StorageError("storage.toml version must be 1")
    content = config.get("content")
    sources = config.get("sources")
    if not isinstance(content, dict) or not isinstance(sources, dict):
        raise StorageError("storage.toml requires [content] and [sources]")
    formats = content.get("formats")
    if not isinstance(formats, list) or not formats or not all(
        isinstance(value, str) and value for value in formats
    ):
        raise StorageError("content.formats must be a non-empty string list")
    if len(formats) != len(set(formats)):
        raise StorageError("content.formats contains duplicates")
    default = content.get("default_source")
    if not isinstance(default, str) or default not in sources:
        raise StorageError("content.default_source must name a configured source")
    for source in sources:
        source_spec(config, source)
    return config


def normalized_routes(
    config_path: Path,
    config: dict[str, Any],
    source: str,
) -> list[dict[str, Any]]:
    spec = source_spec(config, source)
    manifest_path = configured_path(config_path, spec["routes"])
    manifest = load_toml(manifest_path)
    if manifest.get("version") != 1:
        raise StorageError(f"route manifest version must be 1: {manifest_path}")
    raw_routes = manifest.get("route", [])
    if not isinstance(raw_routes, list) or not all(
        isinstance(item, dict) for item in raw_routes
    ):
        raise StorageError(f"route entries must be tables: {manifest_path}")

    routes: list[dict[str, Any]] = []
    ids: dict[str, str] = {}
    paths: dict[str, str] = {}
    seen: set[tuple[str, str]] = set()
    for raw in raw_routes:
        node_id = normalize_id(raw.get("id"))
        rooted_path = normalize_path(raw.get("path"))
        content_format = raw.get("format")
        if content_format not in config["content"]["formats"]:
            raise StorageError(f"invalid route format: {content_format!r}")
        if node_id in ids and ids[node_id] != rooted_path:
            raise StorageError(f"source {source!r} maps one id to several paths")
        if rooted_path in paths and paths[rooted_path] != node_id:
            raise StorageError(f"source {source!r} maps one path to several ids")
        identity = (node_id, content_format)
        if identity in seen:
            raise StorageError(f"duplicate {source!r} route for {identity!r}")
        ids[node_id] = rooted_path
        paths[rooted_path] = node_id
        seen.add(identity)
        routes.append(
            {
                **raw,
                "id": node_id,
                "path": rooted_path,
                "format": content_format,
                "source": source,
            }
        )
    return routes


def all_routes(
    config_path: Path,
    config: dict[str, Any],
    *,
    include_disabled: bool = False,
) -> list[dict[str, Any]]:
    routes: list[dict[str, Any]] = []
    for source in sorted(config["sources"]):
        spec = source_spec(config, source)
        if spec["enabled"] or include_disabled:
            routes.extend(normalized_routes(config_path, config, source))
    return routes


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def materialize(
    config_path: Path,
    config: dict[str, Any],
    route: dict[str, Any],
) -> dict[str, Any] | None:
    spec = source_spec(config, route["source"])
    replica = {
        key: route[key] for key in ("id", "path", "format", "source")
    }
    if spec["kind"] == "directory":
        location = route.get("location")
        if not isinstance(location, str) or not location:
            raise StorageError(f"local route requires location: {route['id']}")
        root = configured_path(config_path, spec["root"])
        candidate = (root / location).resolve()
        try:
            candidate.relative_to(root)
        except ValueError as exc:
            raise StorageError("resolved location escapes its storage root") from exc
        if not candidate.is_file():
            return None
        stat = candidate.stat()
        return {
            **replica,
            "uri": candidate.as_uri(),
            "modified_at": datetime.fromtimestamp(
                stat.st_mtime, tz=timezone.utc
            ).isoformat(),
            "sha256": sha256(candidate),
            "size": stat.st_size,
        }

    uri = route.get("uri")
    if not isinstance(uri, str) or not uri:
        raise StorageError(f"remote route requires uri: {route['id']}")
    replica["uri"] = uri
    for field in ("modified_at", "sha256", "size"):
        if field in route:
            replica[field] = route[field]
    return replica


def matching_routes(
    config_path: Path,
    config: dict[str, Any],
    *,
    node_id: str | None,
    rooted_path: str | None,
    content_format: str | None,
) -> list[dict[str, Any]]:
    node_id, rooted_path = normalize_selector(node_id, rooted_path)
    if content_format is not None and content_format not in config["content"]["formats"]:
        raise StorageError(f"invalid format: {content_format!r}")
    routes = all_routes(config_path, config)
    matches = [
        route
        for route in routes
        if (node_id is None or route["id"] == node_id)
        and (rooted_path is None or route["path"] == rooted_path)
        and (content_format is None or route["format"] == content_format)
    ]
    if node_id is not None and rooted_path is not None and not matches:
        id_exists = any(route["id"] == node_id for route in routes)
        path_exists = any(route["path"] == rooted_path for route in routes)
        if id_exists or path_exists:
            raise StorageError("id and path do not identify the same route")
    return matches


def replicas(
    config_path: Path,
    config: dict[str, Any],
    *,
    node_id: str | None = None,
    rooted_path: str | None = None,
    content_format: str | None = None,
) -> list[dict[str, Any]]:
    return [
        replica
        for route in matching_routes(
            config_path,
            config,
            node_id=node_id,
            rooted_path=rooted_path,
            content_format=content_format,
        )
        if (replica := materialize(config_path, config, route)) is not None
    ]


def discover_storages(config: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "name": source,
            "kind": source_spec(config, source)["kind"],
            "enabled": source_spec(config, source)["enabled"],
        }
        for source in sorted(config["sources"])
    ]


def resolve(
    config_path: Path,
    config: dict[str, Any],
    *,
    node_id: str | None,
    rooted_path: str | None,
    source: str | None,
    content_format: str | None,
) -> dict[str, Any]:
    selected_source = source or config["content"]["default_source"]
    spec = source_spec(config, selected_source)
    if not spec["enabled"]:
        raise StorageError(f"source {selected_source!r} is disabled")
    matches = [
        item
        for item in replicas(
            config_path,
            config,
            node_id=node_id,
            rooted_path=rooted_path,
            content_format=content_format,
        )
        if item["source"] == selected_source
    ]
    if not matches:
        raise StorageError(f"content not found on source {selected_source!r}")
    if len(matches) > 1:
        choices = ", ".join(item["format"] for item in matches)
        raise StorageError(f"multiple formats found: {choices}; pass --format")
    return matches[0]


def parse_timestamp(value: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise StorageError(f"invalid modified_at timestamp: {value!r}") from exc
    if parsed.tzinfo is None:
        raise StorageError(f"modified_at timestamp requires a timezone: {value!r}")
    return parsed.astimezone(timezone.utc)


def replica_status(items: list[dict[str, Any]]) -> dict[str, Any]:
    checksums = [item.get("sha256") for item in items]
    known = [value for value in checksums if isinstance(value, str)]
    in_sync: bool | None = None
    if len(items) > 1 and len(known) == len(items):
        in_sync = len(set(known)) == 1
    paths = {item["path"] for item in items}
    dated = [item for item in items if isinstance(item.get("modified_at"), str)]
    newest_sources: list[str] = []
    if dated:
        values = [(item, parse_timestamp(item["modified_at"])) for item in dated]
        newest = max(value for _, value in values)
        newest_sources = [item["source"] for item, value in values if value == newest]
    return {
        "available": bool(items),
        "in_sync": in_sync,
        "path_consistent": len(paths) <= 1,
        "newest_sources": newest_sources,
        "replicas": items,
    }


def audit(config_path: Path, config: dict[str, Any]) -> dict[str, Any]:
    identities = sorted(
        {(route["id"], route["format"]) for route in all_routes(config_path, config)}
    )
    objects: list[dict[str, Any]] = []
    for node_id, content_format in identities:
        status = replica_status(
            replicas(
                config_path,
                config,
                node_id=node_id,
                content_format=content_format,
            )
        )
        objects.append({"id": node_id, "format": content_format, **status})
    return {
        "summary": {
            "objects": len(objects),
            "synced": sum(item["in_sync"] is True for item in objects),
            "drifted": sum(item["in_sync"] is False for item in objects),
            "path_drift": sum(not item["path_consistent"] for item in objects),
            "single_source": sum(len(item["replicas"]) == 1 for item in objects),
            "unavailable": sum(not item["available"] for item in objects),
            "unknown": sum(
                len(item["replicas"]) > 1 and item["in_sync"] is None
                for item in objects
            ),
        },
        "objects": objects,
    }


def print_payload(payload: Any, as_json: bool) -> None:
    if as_json or isinstance(payload, dict):
        print(json.dumps(payload, indent=2, sort_keys=True))
    elif isinstance(payload, list):
        for item in payload:
            print("\t".join(f"{key}={value}" for key, value in item.items()))
    else:
        print(payload)


def add_selector_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--id", dest="node_id")
    parser.add_argument("--path", dest="rooted_path")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Discover and resolve Cohesian Research storage"
    )
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    commands = parser.add_subparsers(dest="command", required=True)

    storages = commands.add_parser("storages", help="discover configured storages")
    storages.add_argument("--json", action="store_true")

    listing = commands.add_parser("list", help="list available content replicas")
    add_selector_arguments(listing)
    listing.add_argument("--format", dest="content_format")
    listing.add_argument("--json", action="store_true")

    resolving = commands.add_parser("resolve", help="resolve content to a URI")
    add_selector_arguments(resolving)
    resolving.add_argument("--source")
    resolving.add_argument("--format", dest="content_format")
    resolving.add_argument("--json", action="store_true")

    status = commands.add_parser("status", help="compare content replicas")
    add_selector_arguments(status)
    status.add_argument("--format", dest="content_format")
    status.add_argument("--json", action="store_true")

    auditing = commands.add_parser("audit", help="compare the full storage inventory")
    auditing.add_argument("--json", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config_path = args.config.resolve()
    try:
        config = load_config(config_path)
        if args.command == "storages":
            print_payload(discover_storages(config), args.json)
            return 0
        if args.command == "audit":
            print_payload(audit(config_path, config), args.json)
            return 0
        if args.command == "resolve":
            item = resolve(
                config_path,
                config,
                node_id=args.node_id,
                rooted_path=args.rooted_path,
                source=args.source,
                content_format=args.content_format,
            )
            print_payload(item if args.json else item["uri"], args.json)
            return 0
        items = replicas(
            config_path,
            config,
            node_id=args.node_id,
            rooted_path=args.rooted_path,
            content_format=args.content_format,
        )
        print_payload(replica_status(items) if args.command == "status" else items, args.json)
        return 0
    except StorageError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
