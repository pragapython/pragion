"""Horizontal container widget."""

from __future__ import annotations

from .container import Container


class Row(Container):
    """A horizontal container for child widgets."""

    orientation = "horizontal"
