"""Carbon Binder — one contract, many composable structures.

This is the Cohesian visual-language revision of the original scene.  The
mathematical source of truth is the Carbon Binder paper in Research; this file
owns only its audiovisual interpretation.
"""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from manim import (
    Arrow,
    Circle,
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
    CANVAS,
    CANVAS_DEEP,
    GOLD,
    INK,
    MUTED,
    ORANGE_DARK,
    SHELL,
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


def _binder_node(
    tex: str,
    point: np.ndarray,
    *,
    selected: bool = False,
    radius: float = 0.14,
    font_size: int = 25,
) -> VGroup:
    """Build a scene-local labelled concretion of the common binder ``C``."""
    marker = relation_node(point, radius=radius, selected=selected)
    label = MathTex(tex, font_size=font_size, color=INK).next_to(
        marker,
        np.array([0.0, -1.0, 0.0]),
        buff=0.13,
    )
    return VGroup(marker, label).set_z_index(2)


def _edge(start: np.ndarray, end: np.ndarray, *, width: float = 3.0) -> Line:
    return Line(start, end, color=MUTED, stroke_width=width).set_z_index(0)


def _diagram_title(text: str, point: np.ndarray) -> Text:
    return Text(
        text.upper(),
        font="Avenir Next",
        font_size=20,
        weight="MEDIUM",
        color=ORANGE_DARK,
    ).move_to(point)


def _shape_gallery() -> VGroup:
    """Show three graph shapes admitted by the same local contract."""
    # Chain.
    chain_points = [
        np.array([-5.55, 0.10, 0.0]),
        np.array([-4.35, 0.10, 0.0]),
        np.array([-3.15, 0.10, 0.0]),
    ]
    chain_edges = VGroup(*[_edge(a, b) for a, b in zip(chain_points, chain_points[1:])])
    chain_nodes = VGroup(*[_binder_node("C", point, radius=0.11, font_size=21) for point in chain_points])
    chain = VGroup(
        _diagram_title("chain", np.array([-4.35, 1.35, 0.0])),
        chain_edges,
        chain_nodes,
    )

    # Branch.
    branch_points = [
        np.array([0.0, 0.90, 0.0]),
        np.array([-1.05, -0.45, 0.0]),
        np.array([0.0, -0.75, 0.0]),
        np.array([1.05, -0.45, 0.0]),
    ]
    branch_edges = VGroup(*[_edge(branch_points[0], point) for point in branch_points[1:]])
    branch_nodes = VGroup(
        _binder_node("C", branch_points[0], selected=True, radius=0.13, font_size=22),
        *[_binder_node("C", point, radius=0.11, font_size=21) for point in branch_points[1:]],
    )
    branch = VGroup(
        _diagram_title("branch", np.array([0.0, 1.85, 0.0])),
        branch_edges,
        branch_nodes,
    )

    # Ring.
    centre = np.array([4.35, 0.05, 0.0])
    ring_points = [
        centre + np.array([np.cos(angle), np.sin(angle), 0.0]) * 1.0
        for angle in np.linspace(np.pi / 2, np.pi / 2 + 2 * np.pi, 5, endpoint=False)
    ]
    ring_edges = VGroup(
        *[_edge(ring_points[i], ring_points[(i + 1) % len(ring_points)]) for i in range(len(ring_points))]
    )
    ring_nodes = VGroup(*[_binder_node("C", point, radius=0.10, font_size=20) for point in ring_points])
    ring = VGroup(
        _diagram_title("ring", np.array([4.35, 1.85, 0.0])),
        ring_edges,
        ring_nodes,
    )
    return VGroup(chain, branch, ring)


def _composite_and_decorator() -> VGroup:
    """Build the two orthogonal construction axes from the paper."""
    # Composite: one object contains several objects, and remains a C.
    box = RoundedRectangle(
        width=4.65,
        height=2.65,
        corner_radius=0.22,
        color=ORANGE_DARK,
        stroke_width=2.8,
        fill_color=CANVAS_DEEP,
        fill_opacity=0.74,
    ).move_to(np.array([-3.25, 0.0, 0.0]))
    parent_point = np.array([-3.25, 0.72, 0.0])
    child_points = [
        np.array([-4.55, -0.55, 0.0]),
        np.array([-3.25, -0.55, 0.0]),
        np.array([-1.95, -0.55, 0.0]),
    ]
    composite_edges = VGroup(*[_edge(parent_point, point, width=2.5) for point in child_points])
    composite_nodes = VGroup(
        _binder_node("Comp", parent_point, selected=True, radius=0.14, font_size=23),
        *[
            _binder_node(rf"C_{index}", point, radius=0.11, font_size=21)
            for index, point in enumerate(child_points, start=1)
        ],
    )
    composite = VGroup(box, composite_edges, composite_nodes)

    # Decorator: one object wraps one object, and the result remains a C.
    decorator_point = np.array([3.25, 0.0, 0.0])
    core = _binder_node("C", decorator_point, selected=True, radius=0.14, font_size=23)
    rings = VGroup(
        Circle(radius=0.58, color=GOLD, stroke_width=3.2).move_to(decorator_point),
        Circle(radius=0.93, color=ORANGE_DARK, stroke_width=3.0).move_to(decorator_point),
        Circle(radius=1.28, color=SHELL, stroke_width=3.0).move_to(decorator_point),
    )
    rings[0].set_fill(GOLD, opacity=0.06)
    decorator_name = MathTex(r"Dec(Dec(C))", font_size=25, color=INK).move_to(
        decorator_point + np.array([0.0, -1.72, 0.0])
    )
    decorator = VGroup(rings, core, decorator_name)
    return VGroup(composite, decorator)


def _specializations() -> VGroup:
    root_point = np.array([-2.8, 0.0, 0.0])
    type_point = np.array([1.35, 1.15, 0.0])
    query_point = np.array([1.35, -1.15, 0.0])
    arrows = VGroup(
        Arrow(root_point, type_point, buff=0.30, color=MUTED, stroke_width=3.2),
        Arrow(root_point, query_point, buff=0.30, color=MUTED, stroke_width=3.2),
    ).set_z_index(0)
    nodes = VGroup(
        _binder_node("C", root_point, selected=True, radius=0.19, font_size=29),
        _binder_node("T", type_point, radius=0.16, font_size=27),
        _binder_node("Q", query_point, radius=0.16, font_size=27),
    )
    return VGroup(arrows, nodes)


class CarbonBinder(LociVoiceoverScene):
    def construct(self):
        setup_cohesian_voiceover(self)
        apply_scene_style(self)

        seed = make_seed_pod()
        self.add(seed)
        self.wait(0.5)
        play_seed_departure(self, seed)

        chapter = chapter_label("carbon binder")
        equation = equation_label(r"x:C")
        caption = body_caption("one contract  •  many concretions")

        root_point = np.array([0.0, 1.00, 0.0])
        child_points = [
            np.array([-4.15, -0.65, 0.0]),
            np.array([-1.40, -0.65, 0.0]),
            np.array([1.40, -0.65, 0.0]),
            np.array([4.15, -0.65, 0.0]),
        ]
        root = _binder_node("C", root_point, selected=True, radius=0.20, font_size=30)
        interface_edges = VGroup(*[_edge(root_point, point) for point in child_points])
        concretions = VGroup(
            *[
                _binder_node(rf"C_{index}", point, radius=0.14, font_size=25)
                for index, point in enumerate(child_points, start=1)
            ]
        )
        interface = VGroup(root, interface_edges, concretions)

        with self.voiceover(
            text=(
                "Carbon Binder begins with a common interface, C. Any admitted form is written "
                "x colon C. The forms may differ internally, but each one exposes the same local "
                "bonding contract."
            )
        ) as tracker:
            self.play(
                FadeIn(chapter),
                FadeIn(equation),
                FadeIn(caption),
                FadeIn(root, scale=0.65),
                run_time=tracker.duration * 0.34,
            )
            self.play(
                LaggedStart(*[Create(edge) for edge in interface_edges], lag_ratio=0.10),
                LaggedStart(*[FadeIn(node, scale=0.65) for node in concretions], lag_ratio=0.10),
                run_time=tracker.duration * 0.54,
            )
            self.play(Indicate(root, color=GOLD), run_time=tracker.duration * 0.12)
        lecture_pause(self, 1.2)

        shapes = _shape_gallery()
        shapes_equation = equation_label(r"C\to\{\mathrm{chain},\mathrm{branch},\mathrm{ring}\}")
        shapes_caption = body_caption("the analogy is structural")
        with self.voiceover(
            text=(
                "That common surface supports different graph shapes: a chain, a branch, or a ring. "
                "This is the carbon analogy: one reusable bonding surface can generate many "
                "structures. It is a structural analogy, not a model of chemistry."
            )
        ) as tracker:
            self.play(
                FadeOut(interface),
                Transform(equation, shapes_equation),
                Transform(caption, shapes_caption),
                run_time=tracker.duration * 0.22,
            )
            self.play(
                LaggedStart(*[FadeIn(diagram, shift=np.array([0.0, 0.18, 0.0])) for diagram in shapes], lag_ratio=0.18),
                run_time=tracker.duration * 0.78,
            )
        lecture_pause(self, 1.3)

        axes = _composite_and_decorator()
        axes_equation = equation_label(r"Comp(C_1,\ldots,C_n):C\qquad Dec(C):C")
        axes_caption = body_caption("containment  ⟂  wrapping")
        with self.voiceover(
            text=(
                "Two construction axes are especially useful. Composite grows by one-to-many "
                "containment. Decorator grows by wrapping one component around another. The axes "
                "are independent, and both preserve the interface C."
            )
        ) as tracker:
            self.play(
                FadeOut(shapes),
                Transform(equation, axes_equation),
                Transform(caption, axes_caption),
                run_time=tracker.duration * 0.22,
            )
            self.play(FadeIn(axes[0]), run_time=tracker.duration * 0.39)
            self.play(FadeIn(axes[1]), run_time=tracker.duration * 0.39)
        lecture_pause(self, 1.4)

        specializations = _specializations()
        specialization_equation = equation_label(r"C\Rightarrow T\qquad C\Rightarrow Q")
        specialization_caption = body_caption("one interface  •  domain specializations")
        with self.voiceover(
            text=(
                "A domain can then specialize the binder: toward T for types, or Q for queries. "
                "Carbon Binder is the invariant beneath them: many concrete structures, composed "
                "through one shared contract."
            )
        ) as tracker:
            self.play(
                FadeOut(axes),
                Transform(equation, specialization_equation),
                Transform(caption, specialization_caption),
                run_time=tracker.duration * 0.26,
            )
            self.play(
                FadeIn(specializations[1][0], scale=0.65),
                LaggedStart(*[GrowArrow(arrow) for arrow in specializations[0]], lag_ratio=0.14),
                LaggedStart(*[FadeIn(node, scale=0.65) for node in specializations[1][1:]], lag_ratio=0.16),
                run_time=tracker.duration * 0.58,
            )
            self.play(
                Indicate(specializations[1][0], color=GOLD),
                run_time=tracker.duration * 0.16,
            )
        lecture_pause(self, 1.2)

        self.play(
            FadeOut(VGroup(chapter, equation, caption, specializations)),
            run_time=0.45,
        )
        play_seed_arrival(self, run_time=0.55)
        self.wait(0.6)
