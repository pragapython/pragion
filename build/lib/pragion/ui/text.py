"""Text widget for the UI engine."""

from __future__ import annotations

from .widget import Widget


class Text(Widget):
    """A text widget."""

    def __init__(self, text: str, *, id: str | None = None, visible: bool = True, enabled: bool = True) -> None:
        super().__init__(id=id, visible=visible, enabled=enabled)
        self.text = text
        self.type_name = "Text"
