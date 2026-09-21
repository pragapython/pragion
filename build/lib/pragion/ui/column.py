"""Vertical container widget."""

from __future__ import annotations

from .container import Container


class Column(Container):
    """A vertical container for child widgets."""

    orientation = "vertical"
