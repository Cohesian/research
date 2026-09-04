"""Type Binder — a type universe held together by one interface ``T``.

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


def _typed_node(
    tex: str,
    point: np.ndarray,
    *,
    selected: bool = False,
    radius: float = 0.14,
    font_size: int = 25,
    category_path: str | None = None,
) -> VGroup:
    marker = relation_node(point, radius=radius, selected=selected)
    label = MathTex(tex, font_size=font_size, color=INK).next_to(
        marker,
        np.array([0.0, -1.0, 0.0]),
        buff=0.13,
    )
    parts = [marker, label]
    if category_path is not None:
        category = MathTex(category_path, font_size=16, color=MUTED).next_to(
            label,
            np.array([0.0, -1.0, 0.0]),
            buff=0.08,
        )
        parts.append(category)
    return VGroup(*parts).set_z_index(2)


def _edge(start: np.ndarray, end: np.ndarray, *, width: float = 2.8) -> Line:
    return Line(start, end, color=MUTED, stroke_width=width).set_z_index(0)


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
    root_point = np.array([0.0, 1.65, 0.0])
    type_point = np.array([-3.1, 0.63, 0.0])
    decorator_point = np.array([3.1, 0.63, 0.0])
    leaf_point = np.array([-4.35, -0.43, 0.0])
    composite_point = np.array([-1.85, -0.43, 0.0])
    leaf_points = [
        np.array([-5.45, -1.60, 0.0]),
        np.array([-4.72, -1.60, 0.0]),
        np.array([-3.98, -1.60, 0.0]),
        np.array([-3.25, -1.60, 0.0]),
    ]
    composite_points = [
        np.array([-2.25, -1.60, 0.0]),
        np.array([-1.45, -1.60, 0.0]),
    ]
    decorator_points = [
        np.array([2.65, -0.67, 0.0]),
        np.array([3.55, -0.67, 0.0]),
    ]

    root = _typed_node("T", root_point, selected=True, radius=0.17, font_size=28)
    families = VGroup(
        _category("t", type_point, selected=True),
        _category("d", decorator_point),
        _category("l", leaf_point),
        _category("c", composite_point),
    )
    concretes = VGroup(
        *[
            _typed_node(tex, point, radius=0.10, font_size=20)
            for tex, point in zip(("i", "f", "b", "s"), leaf_points)
        ],
        *[
            _typed_node(tex, point, radius=0.11, font_size=21)
            for tex, point in zip(("m", "a"), composite_points)
        ],
        *[
            _typed_node(tex, point, radius=0.12, font_size=23)
            for tex, point in zip(("r", "v"), decorator_points)
        ],
    )
    edges = VGroup(
        _edge(root_point, type_point),
        _edge(root_point, decorator_point),
        _edge(type_point, leaf_point),
        _edge(type_point, composite_point),
        *[_edge(leaf_point, point, width=2.2) for point in leaf_points],
        *[_edge(composite_point, point, width=2.2) for point in composite_points],
        *[_edge(decorator_point, point, width=2.2) for point in decorator_points],
    )
    type_title = Text(
        "TYPE SHAPE",
        font="Avenir Next",
        font_size=18,
        weight="MEDIUM",
        color=ORANGE_DARK,
    ).move_to(np.array([-3.1, 2.25, 0.0]))
    decorator_title = Text(
        "WRAPPER",
        font="Avenir Next",
        font_size=18,
        weight="MEDIUM",
        color=ORANGE_DARK,
    ).move_to(np.array([3.1, 2.25, 0.0]))
    return VGroup(edges, root, families, concretes, type_title, decorator_title)


def _orthogonal_constructors() -> VGroup:
    # This is one projection of the relations, not their definition.
    composite_root = np.array([-5.05, 0.0, 0.0])
    child_points = [
        np.array([-2.35, 1.10, 0.0]),
        np.array([-2.35, 0.0, 0.0]),
        np.array([-2.35, -1.10, 0.0]),
    ]
    composite = VGroup(
        VGroup(*[_edge(composite_root, point, width=2.8) for point in child_points]),
        _typed_node("a", composite_root, selected=True, radius=0.16, font_size=27),
        VGroup(
            *[
                _typed_node(rf"T_{index}", point, radius=0.11, font_size=21)
                for index, point in enumerate(child_points, start=1)
            ]
        ),
    )

    decorator_points = [
        np.array([3.35, 1.20, 0.0]),
        np.array([3.35, 0.0, 0.0]),
        np.array([3.35, -1.20, 0.0]),
    ]
    decorator = VGroup(
        VGroup(
            _edge(decorator_points[0], decorator_points[1], width=2.8),
            _edge(decorator_points[1], decorator_points[2], width=2.8),
        ),
        VGroup(
            _typed_node("r", decorator_points[0], radius=0.13, font_size=24),
            _typed_node("v", decorator_points[1], radius=0.13, font_size=24),
            _typed_node("T", decorator_points[2], selected=True, radius=0.14, font_size=25),
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


def _combined_example() -> VGroup:
    root_point = np.array([-5.10, 0.0, 0.0])
    remover_points = [
        np.array([-3.35, 1.20, 0.0]),
        np.array([-3.35, -1.20, 0.0]),
    ]
    validator_points = [
        np.array([-1.35, 1.20, 0.0]),
        np.array([-1.35, -1.20, 0.0]),
    ]
    upper_leaf = np.array([0.65, 1.20, 0.0])
    nested_array = np.array([0.65, -1.20, 0.0])
    nested_leaves = [
        np.array([2.85, -0.58, 0.0]),
        np.array([2.85, -1.72, 0.0]),
    ]

    primary_composite_edges = VGroup(
        *[_edge(root_point, point, width=2.8) for point in remover_points]
    )
    nested_composite_edges = VGroup(
        *[_edge(nested_array, point, width=2.8) for point in nested_leaves]
    )
    decorator_edges = VGroup(
        Line(remover_points[0], validator_points[0], color=ORANGE_DARK, stroke_width=3.6),
        Line(validator_points[0], upper_leaf, color=ORANGE_DARK, stroke_width=3.6),
        Line(remover_points[1], validator_points[1], color=ORANGE_DARK, stroke_width=3.6),
        Line(validator_points[1], nested_array, color=ORANGE_DARK, stroke_width=3.6),
    ).set_z_index(0)
    root = _typed_node(
        "m",
        root_point,
        selected=True,
        radius=0.18,
        font_size=29,
        category_path=r"T\to t\to c",
    )
    first_children = VGroup(
        *[
            _typed_node("r", point, radius=0.13, font_size=24, category_path=r"T\to d")
            for point in remover_points
        ]
    )
    decorator_nodes = VGroup(
        _typed_node("v", validator_points[0], radius=0.13, font_size=24, category_path=r"T\to d"),
        _typed_node(
            "i",
            upper_leaf,
            selected=True,
            radius=0.14,
            font_size=25,
            category_path=r"T\to t\to l",
        ),
        _typed_node("v", validator_points[1], radius=0.13, font_size=24, category_path=r"T\to d"),
        _typed_node(
            "a",
            nested_array,
            selected=True,
            radius=0.14,
            font_size=25,
            category_path=r"T\to t\to c",
        ),
    )
    nested_nodes = VGroup(
        _typed_node("i", nested_leaves[0], radius=0.12, font_size=23, category_path=r"T\to t\to l"),
        _typed_node("f", nested_leaves[1], radius=0.12, font_size=23, category_path=r"T\to t\to l"),
    )
    key_labels = VGroup(
        MathTex("x", font_size=20, color=MUTED).move_to(np.array([-4.23, 0.83, 0.0])),
        MathTex("y", font_size=20, color=MUTED).move_to(np.array([-4.23, -0.83, 0.0])),
    )
    decorated_integer = MathTex(r"r\{v\{i\}\}:T", font_size=24, color=INK).move_to(
        np.array([-1.35, 2.02, 0.0])
    )
    legend = VGroup(
        Line(np.array([3.85, 1.12, 0.0]), np.array([4.55, 1.12, 0.0]), color=MUTED, stroke_width=2.8),
        Text("composite", font="Avenir Next", font_size=17, color=MUTED).move_to(
            np.array([5.15, 1.12, 0.0])
        ),
        Line(
            np.array([3.85, 0.54, 0.0]),
            np.array([4.55, 0.54, 0.0]),
            color=ORANGE_DARK,
            stroke_width=3.6,
        ),
        Text("decorator", font="Avenir Next", font_size=17, color=ORANGE_DARK).move_to(
            np.array([5.15, 0.54, 0.0])
        ),
    )
    return VGroup(
        primary_composite_edges,
        nested_composite_edges,
        decorator_edges,
        root,
        first_children,
        decorator_nodes,
        nested_nodes,
        key_labels,
        decorated_integer,
        legend,
    )


class TypeBinder(LociVoiceoverScene):
    def construct(self):
        setup_cohesian_voiceover(self)
        apply_scene_style(self)

        seed = make_seed_pod()
        self.add(seed)
        self.wait(0.5)
        play_seed_departure(self, seed)

        chapter = chapter_label("type binder")
        equation = equation_label(r"C\Rightarrow T\qquad X:T")
        caption = body_caption("the binder of a type universe")

        c_point = np.array([-2.45, 0.0, 0.0])
        t_point = np.array([2.45, 0.0, 0.0])
        specialization = VGroup(
            Arrow(c_point, t_point, buff=0.34, color=MUTED, stroke_width=3.2).set_z_index(0),
            _typed_node("C", c_point, radius=0.17, font_size=28),
            _typed_node("T", t_point, selected=True, radius=0.20, font_size=30),
        )

        with self.voiceover(
            text=(
                "Type Binder specializes Carbon Binder's common interface. C becomes T: the binder "
                "of a type universe. Every admitted form is written X colon T, regardless of its "
                "internal shape."
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
        taxonomy_equation = equation_label(r"T::=t\mid d\{T\}")
        taxonomy_caption = body_caption("t: type shape  •  d: wrapper")
        with self.voiceover(
            text=(
                "Inside T, two families remain distinct. The type family t describes shape: leaves "
                "such as int, float, bool, and string, or composites such as map and array. The "
                "decorator family d contains wrappers: remover and validator."
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
                    FadeIn(taxonomy[5]),
                    lag_ratio=0.10,
                ),
                run_time=tracker.duration * 0.80,
            )
        lecture_pause(self, 1.3)

        constructors = _orthogonal_constructors()
        constructors_equation = equation_label(r"c[T_1,\ldots,T_n]:t\qquad d\{T\}:T")
        constructors_caption = body_caption("independent relations  •  different arities")
        with self.voiceover(
            text=(
                "Composite and decorator are independent relations, not prescribed drawings. Here, "
                "the composite relation branches from one node to many T values, while the decorator "
                "relation forms a one-to-one chain. Either could also be drawn as nested containers."
            )
        ) as tracker:
            self.play(
                FadeOut(taxonomy),
                Transform(equation, constructors_equation),
                Transform(caption, constructors_caption),
                run_time=tracker.duration * 0.22,
            )
            self.play(FadeIn(constructors[2]), run_time=tracker.duration * 0.12)
            self.play(FadeIn(constructors[0]), run_time=tracker.duration * 0.33)
            self.play(FadeIn(constructors[1]), run_time=tracker.duration * 0.33)
        lecture_pause(self, 1.4)

        nested = _combined_example()
        nested_equation = equation_label(r"m[x:r\{v\{i\}\},\ y:r\{v\{a[i,f]\}\}]:T")
        nested_caption = body_caption("relations alternate while T stays stable")
        with self.voiceover(
            text=(
                "Now combine them in one graph. A map has x and y as composite children. Each branch "
                "is decorated by remover and validator; the upper branch explicitly becomes r of v "
                "of integer. Beneath every node, its category path shows that it is still T. The y "
                "branch reaches an array, which opens a new composite relation to integer and float."
            )
        ) as tracker:
            self.play(
                FadeOut(constructors),
                Transform(equation, nested_equation),
                Transform(caption, nested_caption),
                run_time=tracker.duration * 0.24,
            )
            self.play(
                Create(nested[0]),
                FadeIn(nested[3], scale=0.70),
                FadeIn(nested[4]),
                FadeIn(nested[7]),
                run_time=tracker.duration * 0.20,
            )
            self.play(
                Create(nested[2]),
                LaggedStart(*[FadeIn(value, scale=0.65) for value in nested[5]], lag_ratio=0.12),
                FadeIn(nested[8]),
                run_time=tracker.duration * 0.28,
            )
            self.play(
                Create(nested[1]),
                LaggedStart(*[FadeIn(value, scale=0.65) for value in nested[6]], lag_ratio=0.16),
                FadeIn(nested[9]),
                run_time=tracker.duration * 0.18,
            )
            self.play(
                Indicate(nested[3], color=GOLD),
                Indicate(nested[5][3], color=GOLD),
                run_time=tracker.duration * 0.10,
            )
        lecture_pause(self, 1.2)

        self.play(FadeOut(VGroup(chapter, equation, caption, nested)), run_time=0.45)
        play_seed_arrival(self, run_time=0.55)
        self.wait(0.6)
