"""TLF Composite — corpus shape and traversal projections over fixed nodes.

The mathematical source of truth lives in Research. This scene is its
Cohesian audiovisual interpretation.
"""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from manim import (
    Arrow,
    Create,
    CurvedArrow,
    FadeIn,
    FadeOut,
    GrowArrow,
    Indicate,
    LaggedStart,
    Line,
    MathTex,
    RoundedRectangle,
    Text,
    Transform,
    VGroup,
)
from loci.voiceover import LociVoiceoverScene

from loci_plugins.cohesian import (
    CANVAS_DEEP,
    GOLD,
    INK,
    MUTED,
    ORANGE_DARK,
    apply_scene_style,
    body_caption,
    chapter_label,
    equation_label,
    make_seed_pod,
    play_seed_arrival,
    play_seed_departure,
    relation_node,
)
from _voiceover import lecture_pause, setup_cohesian_voiceover


def _corpus_node(
    kind: str,
    point: np.ndarray,
    *,
    name: str | None = None,
    selected: bool = False,
    category_path: str | None = None,
) -> VGroup:
    radius = {"K": 0.20, "T": 0.16, "L": 0.14, "F": 0.11}.get(kind, 0.14)
    marker = relation_node(point, radius=radius, selected=selected or kind == "T")
    symbol = MathTex(kind, font_size=26 if kind != "K" else 30, color=INK).next_to(
        marker,
        np.array([0.0, -1.0, 0.0]),
        buff=0.12,
    )
    parts = [marker, symbol]
    if category_path is not None:
        category = MathTex(category_path, font_size=15, color=MUTED).next_to(
            symbol,
            np.array([0.0, -1.0, 0.0]),
            buff=0.07,
        )
        parts.append(category)
    if name is not None:
        name_label = Text(
            name,
            font="Avenir Next",
            font_size=15,
            color=INK,
        ).next_to(marker, np.array([1.0, 0.0, 0.0]), buff=0.20)
        parts.append(name_label)
    return VGroup(*parts).set_z_index(3)


def _edge(
    start: np.ndarray,
    end: np.ndarray,
    *,
    color: str = MUTED,
    width: float = 2.7,
) -> Line:
    return Line(start, end, color=color, stroke_width=width).set_z_index(0)


def _category(tex: str, point: np.ndarray, *, selected: bool = False) -> VGroup:
    color = GOLD if selected else ORANGE_DARK
    card = RoundedRectangle(
        width=1.20,
        height=0.76,
        corner_radius=0.14,
        color=color,
        stroke_width=2.6,
        fill_color=CANVAS_DEEP,
        fill_opacity=0.88,
    ).move_to(point)
    label = MathTex(tex, font_size=30, color=INK).move_to(point)
    return VGroup(card, label).set_z_index(2)


def _taxonomy() -> VGroup:
    root_point = np.array([0.0, 1.62, 0.0])
    composite_point = np.array([-2.25, 0.30, 0.0])
    leaf_point = np.array([2.25, 0.30, 0.0])
    topic_point = np.array([-3.20, -1.15, 0.0])
    lecture_point = np.array([-1.30, -1.15, 0.0])
    file_point = np.array([2.25, -1.15, 0.0])

    edges = VGroup(
        _edge(root_point, composite_point),
        _edge(root_point, leaf_point),
        _edge(composite_point, topic_point, width=2.2),
        _edge(composite_point, lecture_point, width=2.2),
        _edge(leaf_point, file_point, width=2.2),
    )
    root = _corpus_node("K", root_point, selected=True)
    categories = VGroup(
        _category("c", composite_point, selected=True),
        _category(r"\ell", leaf_point),
    )
    kinds = VGroup(
        _corpus_node("T", topic_point),
        _corpus_node("L", lecture_point),
        _corpus_node("F", file_point),
    )
    labels = VGroup(
        Text(
            "COMPOSITES",
            font="Avenir Next",
            font_size=18,
            weight="MEDIUM",
            color=ORANGE_DARK,
        ).move_to(np.array([-2.25, 2.22, 0.0])),
        Text(
            "LEAF",
            font="Avenir Next",
            font_size=18,
            weight="MEDIUM",
            color=ORANGE_DARK,
        ).move_to(np.array([2.25, 2.22, 0.0])),
    )
    return VGroup(edges, root, categories, kinds, labels)


def _corpus_example() -> tuple[VGroup, dict[str, np.ndarray]]:
    positions = {
        "math": np.array([0.0, 2.05, 0.0]),
        "foundations": np.array([-2.80, 0.90, 0.0]),
        "map": np.array([3.60, 0.90, 0.0]),
        "axioms": np.array([-5.00, -0.30, 0.0]),
        "algebra": np.array([-2.50, -0.30, 0.0]),
        "proofs": np.array([0.20, -0.30, 0.0]),
        "groups_lecture": np.array([-2.50, -1.45, 0.0]),
        "groups_file": np.array([-2.50, -2.40, 0.0]),
        "induction": np.array([0.20, -1.45, 0.0]),
    }
    kinds = {
        "math": "T",
        "foundations": "L",
        "map": "F",
        "axioms": "F",
        "algebra": "T",
        "proofs": "L",
        "groups_lecture": "L",
        "groups_file": "F",
        "induction": "F",
    }
    names = {
        "math": "math",
        "foundations": "foundations",
        "map": "map",
        "axioms": "axioms",
        "algebra": "algebra",
        "proofs": "proofs",
        "groups_lecture": "groups",
        "groups_file": "groups",
        "induction": "induction",
    }
    grouping_pairs = [
        ("math", "foundations"),
        ("math", "map"),
        ("foundations", "axioms"),
        ("foundations", "algebra"),
        ("foundations", "proofs"),
        ("algebra", "groups_lecture"),
        ("groups_lecture", "groups_file"),
        ("proofs", "induction"),
    ]
    grouping_edges = VGroup(
        *[_edge(positions[source], positions[target]) for source, target in grouping_pairs]
    )
    root = _corpus_node(
        "T",
        positions["math"],
        name=names["math"],
        selected=True,
        category_path=r"K\to c",
    )
    remaining = VGroup(
        *[
            _corpus_node(
                kinds[key],
                positions[key],
                name=names[key],
                category_path=r"K\to c" if kinds[key] in {"T", "L"} else r"K\to\ell",
            )
            for key in positions
            if key != "math"
        ]
    )
    return VGroup(grouping_edges, root, remaining), positions


def _traversal_overlays(positions: dict[str, np.ndarray]) -> VGroup:
    linear_edges = VGroup(
        Arrow(
            positions["axioms"],
            positions["induction"],
            buff=0.20,
            color=ORANGE_DARK,
            stroke_width=3.5,
            max_tip_length_to_length_ratio=0.08,
        ),
        Arrow(
            positions["induction"],
            positions["groups_file"],
            buff=0.20,
            color=ORANGE_DARK,
            stroke_width=3.5,
            max_tip_length_to_length_ratio=0.10,
        ),
    ).set_z_index(1)
    related_edge = CurvedArrow(
        positions["groups_file"],
        positions["axioms"],
        angle=-0.85,
        color=GOLD,
        stroke_width=4.0,
        tip_length=0.16,
    ).set_z_index(1)
    legend = VGroup(
        Line(np.array([3.72, -0.35, 0.0]), np.array([4.42, -0.35, 0.0]), color=MUTED, stroke_width=2.7),
        MathTex(r"E_g", font_size=19, color=INK).move_to(np.array([4.92, -0.35, 0.0])),
        Line(
            np.array([3.72, -0.93, 0.0]),
            np.array([4.42, -0.93, 0.0]),
            color=ORANGE_DARK,
            stroke_width=3.5,
        ),
        MathTex(r"E_l", font_size=19, color=ORANGE_DARK).move_to(np.array([4.92, -0.93, 0.0])),
        Line(np.array([3.72, -1.51, 0.0]), np.array([4.42, -1.51, 0.0]), color=GOLD, stroke_width=4.0),
        MathTex(r"E_r", font_size=19, color=INK).move_to(np.array([4.92, -1.51, 0.0])),
    )
    return VGroup(linear_edges, related_edge, legend)


class TLFComposite(LociVoiceoverScene):
    def construct(self):
        setup_cohesian_voiceover(self)
        apply_scene_style(self)

        seed = make_seed_pod()
        self.add(seed)
        self.wait(0.5)
        play_seed_departure(self, seed)

        chapter = chapter_label("TLF composite")
        equation = equation_label(r"C\Rightarrow K\qquad x:K")
        caption = body_caption("Topic  •  Lecture  •  File")

        c_point = np.array([-2.45, 0.0, 0.0])
        k_point = np.array([2.45, 0.0, 0.0])
        specialization = VGroup(
            Arrow(c_point, k_point, buff=0.34, color=MUTED, stroke_width=3.2).set_z_index(0),
            _corpus_node("C", c_point),
            _corpus_node("K", k_point, selected=True),
        )

        with self.voiceover(
            text=(
                "TLF means Topic, Lecture, and File. Here, Carbon Binder specializes into K: the "
                "shared surface of a knowledge corpus. Every admitted topic, lecture, or file is a "
                "node of that corpus."
            )
        ) as tracker:
            self.play(
                FadeIn(chapter),
                FadeIn(equation),
                FadeIn(caption),
                FadeIn(specialization[1], scale=0.65),
                run_time=tracker.duration * 0.34,
            )
            self.play(
                GrowArrow(specialization[0]),
                FadeIn(specialization[2], scale=0.65),
                run_time=tracker.duration * 0.50,
            )
            self.play(Indicate(specialization[2], color=GOLD), run_time=tracker.duration * 0.16)
        lecture_pause(self, 1.2)

        taxonomy = _taxonomy()
        taxonomy_equation = equation_label(r"K::=F\mid c[K_1,\ldots,K_n],\quad c\in\{T,L\}")
        taxonomy_caption = body_caption("T and L are composites  •  F is a leaf  •  kind is not depth")
        with self.voiceover(
            text=(
                "There are two structural categories. Topics and lectures are composites; files are "
                "leaves. These kinds are labels, not required depth levels. A topic or lecture may "
                "contain any valid mixture of topics, lectures, and files."
            )
        ) as tracker:
            self.play(
                FadeOut(specialization),
                Transform(equation, taxonomy_equation),
                Transform(caption, taxonomy_caption),
                run_time=tracker.duration * 0.20,
            )
            self.play(
                LaggedStart(
                    Create(taxonomy[0]),
                    FadeIn(taxonomy[1], scale=0.65),
                    FadeIn(taxonomy[2]),
                    FadeIn(taxonomy[3]),
                    FadeIn(taxonomy[4]),
                    lag_ratio=0.11,
                ),
                run_time=tracker.duration * 0.80,
            )
        lecture_pause(self, 1.3)

        corpus, positions = _corpus_example()
        shape_equation = equation_label(r"\operatorname{shape}(K)=(V,E_g)")
        shape_caption = body_caption("grouping gives the shape  •  tree realization  •  DAG contract")
        with self.voiceover(
            text=(
                "Now build the paper's corpus using grouping edges E g. Math groups a foundations "
                "lecture and a file directly. That lecture contains a file, another topic, and another "
                "lecture. This mixed nesting is valid because kind is not depth."
            )
        ) as tracker:
            self.play(
                FadeOut(taxonomy),
                Transform(equation, shape_equation),
                Transform(caption, shape_caption),
                run_time=tracker.duration * 0.18,
            )
            self.play(FadeIn(corpus[1], scale=0.65), run_time=tracker.duration * 0.14)
            self.play(
                Create(corpus[0]),
                LaggedStart(*[FadeIn(node, scale=0.65) for node in corpus[2]], lag_ratio=0.07),
                run_time=tracker.duration * 0.68,
            )
        lecture_pause(self, 1.5)

        overlays = _traversal_overlays(positions)
        graph_equation = equation_label(r"G_K=(V,E_g\sqcup E_l\sqcup E_r,\kappa)")
        graph_caption = body_caption("πg ⟂ πl, πr  •  traversal changes  •  grouping remains fixed")
        with self.voiceover(
            text=(
                "Without moving a node, add a linear reading path from axioms to induction to groups. "
                "Then add a related edge from groups back to axioms. These file-to-file overlays change "
                "traversal, not containment. They are projections of the same corpus, while E g alone "
                "continues to own its shape."
            )
        ) as tracker:
            self.play(
                Transform(equation, graph_equation),
                Transform(caption, graph_caption),
                run_time=tracker.duration * 0.18,
            )
            self.play(
                LaggedStart(*[GrowArrow(edge) for edge in overlays[0]], lag_ratio=0.18),
                run_time=tracker.duration * 0.34,
            )
            self.play(
                Create(overlays[1]),
                FadeIn(overlays[2]),
                run_time=tracker.duration * 0.34,
            )
            self.play(
                LaggedStart(
                    *[
                        Indicate(node, color=GOLD, scale_factor=1.12)
                        for node in (corpus[2][2], corpus[2][7], corpus[2][6])
                    ],
                    lag_ratio=0.12,
                ),
                run_time=tracker.duration * 0.14,
            )
        lecture_pause(self, 1.4)

        self.play(FadeOut(VGroup(chapter, equation, caption, corpus, overlays)), run_time=0.45)
        play_seed_arrival(self, run_time=0.55)
        self.wait(0.6)
