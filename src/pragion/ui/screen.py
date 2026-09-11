"""Screen abstraction for the runtime PoC."""

from __future__ import annotations

from .widget import Widget


class Screen(Widget):
    """Base class for a Pragion screen."""

    def __init__(self, *, title: str | None = None) -> None:
        super().__init__(value=title)
        self.title = title
        self.children: list[Widget] = []

    def build(self) -> list[Widget]:
        """Return a list of widgets for this screen."""
        return list(self.children)
