"""Portable voiceover helpers for an accepted Studio scene."""

from __future__ import annotations


def setup_cohesian_voiceover(scene) -> None:
    """Use the speech service selected by this standalone Loci project."""
    scene.setup_voiceover()


def lecture_pause(scene, duration: float) -> None:
    """Hold a completed visual long enough for the preceding idea to settle."""
    if duration <= 0:
        raise ValueError("lecture pause duration must be positive")
    scene.wait(duration)
