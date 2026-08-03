from __future__ import annotations

import hashlib
import tempfile
import unittest
from pathlib import Path

from research_storage.cli import (
    DEFAULT_CONFIG,
    StorageError,
    audit,
    discover_storages,
    load_config,
    normalize_id,
    normalize_path,
    normalized_routes,
    replica_status,
    replicas,
    resolve,
)


NODE_ID = "11111111-1111-4111-8111-111111111111"
NODE_PATH = "T-test/L-example/F-01-paper"

CONFIG = """\
version = 1

[content]
formats = ["md", "ipynb"]
default_source = "local"

[sources.local]
kind = "directory"
enabled = true
root = "local"
routes = "local/routes.toml"

[sources.google-drive]
kind = "remote"
enabled = true
routes = "google-drive/routes.toml"
"""


class StorageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.config_path = self.root / "storage.toml"
        self.config_path.write_text(CONFIG, encoding="utf-8")
        self.local_routes = self.root / "local/routes.toml"
        self.drive_routes = self.root / "google-drive/routes.toml"
        self.local_routes.parent.mkdir(parents=True)
        self.drive_routes.parent.mkdir(parents=True)
        self.document = self.root / "local/T-test/L-example/F-01-paper.md"
        self.document.parent.mkdir(parents=True, exist_ok=True)
        self.document.write_text("# Paper\n", encoding="utf-8")
        self.write_local_routes()
        self.write_drive_routes()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_local_routes(self, *, path: str = NODE_PATH) -> None:
        self.local_routes.write_text(
            f'''version = 1

[[route]]
id = "{NODE_ID}"
path = "{path}"
format = "md"
location = "T-test/L-example/F-01-paper.md"
''',
            encoding="utf-8",
        )

    def write_drive_routes(self, body: str = "") -> None:
        self.drive_routes.write_text(f"version = 1\n{body}", encoding="utf-8")

    def drive_route(self, *, path: str = NODE_PATH) -> str:
        digest = hashlib.sha256(b"# Paper\n").hexdigest()
        return f'''\n[[route]]
id = "{NODE_ID}"
path = "{path}"
format = "md"
uri = "https://drive.google.com/example"
sha256 = "{digest}"
modified_at = "2026-08-03T10:00:00+00:00"
'''

    def test_discovers_enabled_storages(self) -> None:
        config = load_config(self.config_path)
        self.assertEqual(
            discover_storages(config),
            [
                {"name": "google-drive", "kind": "remote", "enabled": True},
                {"name": "local", "kind": "directory", "enabled": True},
            ],
        )

    def test_resolves_local_file_by_id(self) -> None:
        config = load_config(self.config_path)
        item = resolve(
            self.config_path,
            config,
            node_id=NODE_ID,
            rooted_path=None,
            source=None,
            content_format="md",
        )
        self.assertEqual(item["source"], "local")
        self.assertEqual(item["path"], NODE_PATH)
        self.assertEqual(item["uri"], self.document.resolve().as_uri())

    def test_resolves_local_file_by_path(self) -> None:
        config = load_config(self.config_path)
        item = resolve(
            self.config_path,
            config,
            node_id=None,
            rooted_path=NODE_PATH,
            source="local",
            content_format="md",
        )
        self.assertEqual(item["id"], NODE_ID)

    def test_both_selectors_must_identify_the_same_route(self) -> None:
        config = load_config(self.config_path)
        with self.assertRaisesRegex(StorageError, "do not identify the same route"):
            resolve(
                self.config_path,
                config,
                node_id=NODE_ID,
                rooted_path="T-test/L-example/F-99-other",
                source="local",
                content_format="md",
            )

    def test_lists_local_and_drive_replicas(self) -> None:
        self.write_drive_routes(self.drive_route())
        config = load_config(self.config_path)
        items = replicas(
            self.config_path,
            config,
            node_id=NODE_ID,
            content_format="md",
        )
        self.assertEqual({item["source"] for item in items}, {"local", "google-drive"})
        status = replica_status(items)
        self.assertTrue(status["in_sync"])
        self.assertTrue(status["path_consistent"])

    def test_audit_detects_path_drift_between_sources(self) -> None:
        self.write_drive_routes(
            self.drive_route(path="T-test/L-previous/F-01-paper")
        )
        config = load_config(self.config_path)
        result = audit(self.config_path, config)
        self.assertEqual(result["summary"]["objects"], 1)
        self.assertEqual(result["summary"]["path_drift"], 1)
        self.assertFalse(result["objects"][0]["path_consistent"])

    def test_newest_source_uses_replica_timestamp(self) -> None:
        items = [
            {
                "path": NODE_PATH,
                "source": "local",
                "modified_at": "2026-08-01T00:00:00+00:00",
            },
            {
                "path": NODE_PATH,
                "source": "google-drive",
                "modified_at": "2026-08-02T00:00:00+00:00",
            },
        ]
        self.assertEqual(replica_status(items)["newest_sources"], ["google-drive"])

    def test_audit_summarizes_the_full_inventory(self) -> None:
        config = load_config(self.config_path)
        summary = audit(self.config_path, config)["summary"]
        self.assertEqual(summary["objects"], 1)
        self.assertEqual(summary["single_source"], 1)
        self.assertEqual(summary["drifted"], 0)
        self.assertEqual(summary["path_drift"], 0)

    def test_rejects_invalid_selectors(self) -> None:
        with self.assertRaisesRegex(StorageError, "invalid rooted path"):
            normalize_path("../outside")
        with self.assertRaisesRegex(StorageError, "invalid rooted path"):
            normalize_path(None)
        with self.assertRaisesRegex(StorageError, "invalid node id"):
            normalize_id("not-a-uuid")


class RepositoryStorageTests(unittest.TestCase):
    def test_local_routes_cover_the_versioned_corpus(self) -> None:
        config = load_config(DEFAULT_CONFIG)
        routes = normalized_routes(DEFAULT_CONFIG, config, "local")
        local_root = DEFAULT_CONFIG.parent / "local"
        mapped = {route["location"] for route in routes}
        present = {
            path.relative_to(local_root).as_posix()
            for path in local_root.rglob("*")
            if path.is_file() and path.suffix in {".md", ".ipynb"}
        }
        self.assertEqual(mapped, present)
        self.assertEqual(len(routes), 25)


if __name__ == "__main__":
    unittest.main()
