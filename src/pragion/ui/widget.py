"""Widget primitives for the Pragion UI model."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any


class Widget:
    """Base class for Pragion widgets."""

    def __init__(self, value: str | None = None, *, on_click: Callable[[], None] | None = None) -> None:
        self.value = value
        self.on_click = on_click


@dataclass(slots=True)
class Text(Widget):
    """Simple textual widget."""

    value: str = ""
    on_click: Callable[[], None] | None = None


@dataclass(slots=True)
class Button(Widget):
    """Simple clickable button widget."""

    value: str = ""
    on_click: Callable[[], None] | None = None
    payload: dict[str, Any] = field(default_factory=dict)
