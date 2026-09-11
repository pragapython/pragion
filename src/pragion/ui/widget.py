"""Widget primitives for the Pragion UI model."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any


class Widget:
    """Base class for Pragion widgets."""

    def __init__(
        self,
        *,
        id: str | None = None,
        visible: bool = True,
        enabled: bool = True,
        parent: Widget | None = None,
    ) -> None:
        self.id = id or self._generate_id()
        self.visible = visible
        self.enabled = enabled
        self.parent = parent
        self.type_name = self.__class__.__name__

    @staticmethod
    def _generate_id() -> str:
        import uuid

        return uuid.uuid4().hex[:8]


class Text(Widget):
    """Simple textual widget."""

    def __init__(
        self,
        text: str,
        *,
        id: str | None = None,
        visible: bool = True,
        enabled: bool = True,
    ) -> None:
        super().__init__(id=id, visible=visible, enabled=enabled)
        self.text = text
        self.type_name = "Text"


class Button(Widget):
    """Simple clickable button widget."""

    def __init__(
        self,
        text: str,
        *,
        on_click: Callable[[], None] | None = None,
        id: str | None = None,
        visible: bool = True,
        enabled: bool = True,
    ) -> None:
        super().__init__(id=id, visible=visible, enabled=enabled)
        self.text = text
        self.on_click = on_click
        self.type_name = "Button"
        self.payload: dict[str, Any] = {}

    def dispatch_click(self, runtime: Any) -> None:
        """Dispatch click event to the runtime and invoke the callback."""
        if self.on_click is not None:
            self.on_click()
        runtime.emit("button_click", {"widget_id": self.id})
