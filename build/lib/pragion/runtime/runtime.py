"""Runtime orchestration for the Pragion runtime PoC."""

from __future__ import annotations

from typing import Any

from pragion.core.events import Event, EventDispatcher


class Runtime:
    """Minimal runtime that runs the application and dispatches events."""

    def __init__(self) -> None:
        self.dispatcher = EventDispatcher()
        self.events: list[Event] = self.dispatcher.events
        self.running = False

    def emit(self, name: str, payload: dict[str, Any] | None = None) -> Event:
        """Emit a runtime event."""
        return self.dispatcher.dispatch(Event(name=name, payload=payload or {}))

    def dispatch(self, event: Event) -> Event:
        """Dispatch an event to the current runtime bridge."""
        return self.dispatcher.dispatch(event)

    def start(self, app: Any) -> None:
        """Start the application lifecycle."""
        if hasattr(app, "on_start"):
            app.on_start()
        start_target = getattr(app, "start", None)
        if isinstance(start_target, type):
            screen = start_target()
            app.start_screen = screen
            screen.build()
            app.started = True
            app.state = app.Lifecycle.RUNNING
        elif callable(start_target):
            start_target()
        self.running = True
        self.emit("app.started", {"app": app.__class__.__name__})

    def run(self, app: Any) -> None:
        """Compatibility wrapper for launching an application."""
        self.start(app)

    def stop(self) -> None:
        """Stop the runtime in a controlled manner."""
        self.running = False
        self.emit("app.stopped", {})
