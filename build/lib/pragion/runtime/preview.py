"""Local desktop preview for Pragion UI projects."""

from __future__ import annotations

import tkinter as tk
from collections.abc import Callable
from typing import Literal

from pragion.runtime import Runtime
from pragion.ui import Button, Column, Row, Text, Widget


class PreviewWindow:
    """Render the supported Phase 3 widgets in a local Tk window."""

    def __init__(self, root_widget: Widget, runtime: Runtime) -> None:
        self.root_widget = root_widget
        self.runtime = runtime
        try:
            self.window = tk.Tk()
        except tk.TclError as exc:
            raise RuntimeError(
                "No desktop display is available. Run `pragion run` on a local desktop "
                "session, or use `pragion run android` with Android tooling configured."
            ) from exc
        self.window.title("Pragion Preview")
        self.window.geometry("420x260")

    def show(self) -> None:
        """Render the widget tree and block until the preview closes."""
        self._render(self.root_widget, self.window)
        self.window.mainloop()

    def _render(self, widget: Widget, parent: tk.Misc) -> None:
        if not widget.visible:
            return
        if isinstance(widget, Text):
            tk.Label(parent, text=widget.text, anchor="w").pack(fill="x", padx=24, pady=8)
        elif isinstance(widget, Button):
            callback: Callable[[], None] = lambda: widget.dispatch_click(self.runtime)
            tk.Button(parent, text=widget.text, command=callback, state=self._state(widget)).pack(
                pady=10
            )
        elif isinstance(widget, (Column, Row)):
            frame = tk.Frame(parent)
            frame.pack(fill="both", expand=True, padx=16, pady=16)
            for child in widget.children:
                if isinstance(widget, Row):
                    self._render_row_child(child, frame)
                else:
                    self._render(child, frame)

    def _render_row_child(self, widget: Widget, parent: tk.Misc) -> None:
        """Render a row child using horizontal packing."""
        if isinstance(widget, Text):
            tk.Label(parent, text=widget.text).pack(side=tk.LEFT, padx=8, pady=8)
        elif isinstance(widget, Button):
            callback: Callable[[], None] = lambda: widget.dispatch_click(self.runtime)
            tk.Button(parent, text=widget.text, command=callback, state=self._state(widget)).pack(
                side=tk.LEFT, padx=8, pady=8
            )

    @staticmethod
    def _state(widget: Widget) -> Literal["normal", "disabled"]:
        return "normal" if widget.enabled else "disabled"