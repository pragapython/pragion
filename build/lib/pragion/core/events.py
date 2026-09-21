"""Core event definitions used by the runtime and UI layers."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Event:
    """Represents a runtime or UI event passed through Pragion."""

    name: str
    payload: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class EventDispatcher:
    """A minimal dispatcher that stores incoming events."""

    events: list[Event] = field(default_factory=list)

    def dispatch(self, event: Event) -> Event:
        """Capture a dispatched event for runtime processing."""
        self.events.append(event)
        return event
