"""Query Binder — predicates composed through one interface ``Q``.

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


def _query_node(
    tex: str,
    point: np.ndarray,
    *,
    selected: bool = False,
    radius: float = 0.14,
    font_size: int = 25,
    category_path: str | None = None,
    detail: str | None = None,
) -> VGroup:
    marker = relation_node(point, radius=radius, selected=selected)
    symbol = MathTex(tex, font_size=font_size, color=INK).next_to(
        marker,
        np.array([0.0, -1.0, 0.0]),
        buff=0.13,
    )
    parts = [marker, symbol]
    if category_path is not None:
        category = MathTex(category_path, font_size=16, color=MUTED).next_to(
            symbol,
            np.array([0.0, -1.0, 0.0]),
            buff=0.08,
        )
        parts.append(category)
    if detail is not None:
        description = Text(
            detail,
            font="Avenir Next",
            font_size=17,
            color=INK,
        ).next_to(marker, np.array([1.0, 0.0, 0.0]), buff=0.25)
        parts.append(description)
    return VGroup(*parts).set_z_index(2)


def _edge(
    start: np.ndarray,
    end: np.ndarray,
    *,
    color: str = MUTED,
    width: float = 2.8,
) -> Line:
    return Line(start, end, color=color, stroke_width=width).set_z_index(0)


def _category(tex: str, point: np.ndarray, *, selected: bool = False) -> VGroup:
    color = GOLD if selected else ORANGE_DARK
    card = RoundedRectangle(
        width=1.15,
        height=0.74,
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
    category_points = [
        np.array([-3.75, 0.42, 0.0]),
        np.array([0.0, 0.42, 0.0]),
        np.array([3.75, 0.42, 0.0]),
    ]
    leaf_points = [
        np.array([-4.55, -1.05, 0.0]),
        np.array([-3.75, -1.05, 0.0]),
        np.array([-2.95, -1.05, 0.0]),
    ]
    composite_points = [
        np.array([-0.48, -1.05, 0.0]),
        np.array([0.48, -1.05, 0.0]),
    ]
    decorator_point = np.array([3.75, -1.05, 0.0])

    edges = VGroup(
        *[_edge(root_point, point) for point in category_points],
        *[_edge(category_points[0], point, width=2.2) for point in leaf_points],
        *[_edge(category_points[1], point, width=2.2) for point in composite_points],
        _edge(category_points[2], decorator_point, width=2.2),
    )
    root = _query_node("Q", root_point, selected=True, radius=0.18, font_size=29)
    categories = VGroup(
        _category(r"\ell", category_points[0], selected=True),
        _category("c", category_points[1]),
        _category("d", category_points[2]),
    )
    concretes = VGroup(
        *[
            _query_node(tex, point, radius=0.11, font_size=22)
            for tex, point in zip(("e", "g", "h"), leaf_points)
        ],
        *[
            _query_node(tex, point, radius=0.12, font_size=23)
            for tex, point in zip(("a", "o"), composite_points)
        ],
        _query_node("n", decorator_point, radius=0.12, font_size=23),
    )
    titles = VGroup(
        Text("PREDICATE", font="Avenir Next", font_size=18, weight="MEDIUM", color=ORANGE_DARK).move_to(
            np.array([-3.75, 2.22, 0.0])
        ),
        Text("GROUP", font="Avenir Next", font_size=18, weight="MEDIUM", color=ORANGE_DARK).move_to(
            np.array([0.0, 2.22, 0.0])
        ),
        Text("WRAPPER", font="Avenir Next", font_size=18, weight="MEDIUM", color=ORANGE_DARK).move_to(
            np.array([3.75, 2.22, 0.0])
        ),
    )
    return VGroup(edges, root, categories, concretes, titles)


def _independent_relations() -> VGroup:
    composite_root = np.array([-5.05, 0.0, 0.0])
    composite_children = [
        np.array([-2.35, 1.10, 0.0]),
        np.array([-2.35, 0.0, 0.0]),
        np.array([-2.35, -1.10, 0.0]),
    ]
    composite = VGroup(
        VGroup(*[_edge(composite_root, point) for point in composite_children]),
        _query_node("a", composite_root, selected=True, radius=0.16, font_size=27),
        VGroup(
            *[
                _query_node(rf"q_{index}", point, radius=0.11, font_size=21)
                for index, point in enumerate(composite_children, start=1)
            ]
        ),
    )

    decorator_points = [
        np.array([3.35, 0.72, 0.0]),
        np.array([3.35, -0.72, 0.0]),
    ]
    decorator = VGroup(
        _edge(decorator_points[0], decorator_points[1], color=ORANGE_DARK, width=3.6),
        VGroup(
            _query_node("n", decorator_points[0], radius=0.13, font_size=24),
            _query_node("q", decorator_points[1], selected=True, radius=0.14, font_size=25),
        ),
    )
    labels = VGroup(
        Text(
            "COMPOSITE RELATION",
            font="Avenir Next",
            font_size=18,
            weight="MEDIUM",
            color=ORANGE_DARK,
        ).move_to(np.array([-3.70, 2.05, 0.0])),
        Text(
            "DECORATOR RELATION",
            font="Avenir Next",
            font_size=18,
            weight="MEDIUM",
            color=ORANGE_DARK,
        ).move_to(np.array([3.35, 2.05, 0.0])),
    )
    return VGroup(composite, decorator, labels)


def _factual_query() -> VGroup:
    root_point = np.array([-5.20, 0.20, 0.0])
    status_point = np.array([-3.35, 1.65, 0.0])
    not_point = np.array([-3.35, 0.20, 0.0])
    or_point = np.array([-3.35, -1.35, 0.0])
    archived_point = np.array([-0.85, 0.20, 0.0])
    priority_point = np.array([-0.85, -0.92, 0.0])
    score_point = np.array([-0.85, -1.92, 0.0])

    composite_edges = VGroup(
        _edge(root_point, status_point),
        _edge(root_point, not_point),
        _edge(root_point, or_point),
        _edge(or_point, priority_point),
        _edge(or_point, score_point),
    )
    decorator_edge = _edge(not_point, archived_point, color=ORANGE_DARK, width=3.6)
    root = _query_node(
        "a",
        root_point,
        selected=True,
        radius=0.18,
        font_size=29,
        category_path=r"Q\to c",
    )
    first_level = VGroup(
        _query_node(
            "e",
            status_point,
            radius=0.12,
            font_size=23,
            category_path=r"Q\to\ell",
            detail='status = "open"',
        ),
        _query_node("n", not_point, radius=0.13, font_size=24, category_path=r"Q\to d"),
        _query_node("o", or_point, radius=0.13, font_size=24, category_path=r"Q\to c"),
    )
    leaves = VGroup(
        _query_node(
            "e",
            archived_point,
            selected=True,
            radius=0.12,
            font_size=23,
            category_path=r"Q\to\ell",
            detail="archived = true",
        ),
        _query_node(
            "e",
            priority_point,
            radius=0.12,
            font_size=23,
            category_path=r"Q\to\ell",
            detail='priority = "high"',
        ),
        _query_node(
            "g",
            score_point,
            radius=0.12,
            font_size=23,
            category_path=r"Q\to\ell",
            detail="score > 90",
        ),
    )
    legend = VGroup(
        Line(np.array([3.75, 1.20, 0.0]), np.array([4.45, 1.20, 0.0]), color=MUTED, stroke_width=2.8),
        Text("composite", font="Avenir Next", font_size=17, color=MUTED).move_to(
            np.array([5.05, 1.20, 0.0])
        ),
        Line(
            np.array([3.75, 0.62, 0.0]),
            np.array([4.45, 0.62, 0.0]),
            color=ORANGE_DARK,
            stroke_width=3.6,
        ),
        Text("decorator", font="Avenir Next", font_size=17, color=ORANGE_DARK).move_to(
            np.array([5.05, 0.62, 0.0])
        ),
    )
    return VGroup(composite_edges, decorator_edge, root, first_level, leaves, legend)


class QueryBinder(LociVoiceoverScene):
    def construct(self):
        setup_cohesian_voiceover(self)
        apply_scene_style(self)

        seed = make_seed_pod()
        self.add(seed)
        self.wait(0.5)
        play_seed_departure(self, seed)

        chapter = chapter_label("query binder")
        equation = equation_label(r"C\Rightarrow Q\qquad q:Q")
        caption = body_caption("the binder of predicate structures")

        c_point = np.array([-2.45, 0.0, 0.0])
        q_point = np.array([2.45, 0.0, 0.0])
        specialization = VGroup(
            Arrow(c_point, q_point, buff=0.34, color=MUTED, stroke_width=3.2).set_z_index(0),
            _query_node("C", c_point, radius=0.17, font_size=28),
            _query_node("Q", q_point, selected=True, radius=0.20, font_size=30),
        )

        with self.voiceover(
            text=(
                "The binder pattern is not limited to type systems. Query Binder specializes C into "
                "Q: a shared interface for predicates and query structures. Every admitted form is "
                "written q colon Q."
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
        taxonomy_equation = equation_label(r"e,g,h,a,o,n:Q")
        taxonomy_caption = body_caption("predicates  •  groups  •  wrappers")
        with self.voiceover(
            text=(
                "Q has three local categories. Leaves are equality, greater-than, and contains. "
                "Composites are and and or. The decorator is not. These are different operators, "
                "but every concrete node still implements Q."
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

        relations = _independent_relations()
        relations_equation = equation_label(r"a[q_1,\ldots,q_n]:Q\qquad n\{q\}:Q")
        relations_caption = body_caption("independent relations  •  different arities")
        with self.voiceover(
            text=(
                "The relations remain independent. And or or connects one composite to many inner "
                "queries. Not decorates exactly one inner query. The drawing direction may change; "
                "the arity and the relation family do not."
            )
        ) as tracker:
            self.play(
                FadeOut(taxonomy),
                Transform(equation, relations_equation),
                Transform(caption, relations_caption),
                run_time=tracker.duration * 0.22,
            )
            self.play(FadeIn(relations[2]), run_time=tracker.duration * 0.12)
            self.play(FadeIn(relations[0]), run_time=tracker.duration * 0.33)
            self.play(FadeIn(relations[1]), run_time=tracker.duration * 0.33)
        lecture_pause(self, 1.4)

        query = _factual_query()
        query_equation = equation_label(r"\chi:Q")
        query_caption = body_caption("status open  •  not archived  •  priority high or score > 90")
        with self.voiceover(
            text=(
                "Read chi as an and of three branches. First, status equals open. Second, not wraps "
                "archived equals true, using a decorator edge. Third, an or groups priority equals "
                "high with score greater than ninety. Each operator shows its local category path, "
                "and the complete query remains Q."
            )
        ) as tracker:
            self.play(
                FadeOut(relations),
                Transform(equation, query_equation),
                Transform(caption, query_caption),
                run_time=tracker.duration * 0.20,
            )
            self.play(
                Create(query[0]),
                FadeIn(query[2], scale=0.70),
                FadeIn(query[3]),
                run_time=tracker.duration * 0.28,
            )
            self.play(
                Create(query[1]),
                LaggedStart(*[FadeIn(leaf, scale=0.65) for leaf in query[4]], lag_ratio=0.13),
                FadeIn(query[5]),
                run_time=tracker.duration * 0.38,
            )
            self.play(Indicate(query[2], color=GOLD), run_time=tracker.duration * 0.14)
        lecture_pause(self, 1.3)

        self.play(FadeOut(VGroup(chapter, equation, caption, query)), run_time=0.45)
        play_seed_arrival(self, run_time=0.55)
        self.wait(0.6)
