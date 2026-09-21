"""Screen abstraction for the Pragion UI engine."""

from __future__ import annotations

from .column import Column
from .widget import Widget


class Screen(Widget):
    """Base class for a Pragion screen."""

    def __init__(self, *, title: str | None = None, id: str | None = None) -> None:
        super().__init__(id=id)
        self.title = title
        self.type_name = "Screen"

    def build(self) -> Column:
        """Return the root widget for the screen."""
        return Column()

    def ui_tree(self):
        """Convert the screen into a UI tree."""
        from .renderer import Renderer

        return Renderer().render(self.build())
