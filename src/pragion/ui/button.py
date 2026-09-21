"""Button widget for the UI engine."""

from __future__ import annotations

from collections.abc import Callable

from pragion.runtime import Runtime

from .widget import Widget


class Button(Widget):
    """A clickable button widget."""

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

    def dispatch_click(self, runtime: Runtime) -> None:
        """Dispatch click event to the runtime and then invoke the callback."""
        widget_id = self.id
        if self.on_click is not None:
            self.on_click()
        runtime.emit("button_click", {"widget_id": widget_id})
