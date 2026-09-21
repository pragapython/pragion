"""Generic container widget for UI composition."""

from __future__ import annotations

from .widget import Widget


class Container(Widget):
    """A widget that contains other widgets."""

    orientation = "vertical"

    def __init__(
        self,
        *children: Widget,
        id: str | None = None,
        visible: bool = True,
        enabled: bool = True,
    ) -> None:
        super().__init__(id=id, visible=visible, enabled=enabled)
        self.children = list(children)
        for child in self.children:
            child.parent = self
        self.type_name = self.__class__.__name__

    def add(self, child: Widget) -> None:
        """Append a child widget and attach its parent."""
        child.parent = self
        self.children.append(child)
