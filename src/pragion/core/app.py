"""Application base class used by Pragion apps."""

from __future__ import annotations

from enum import Enum


class App:
    """Base application class for Pragion projects."""

    class Lifecycle(str, Enum):
        """Lifecycle states supported in the runtime PoC."""

        CREATED = "CREATED"
        STARTING = "STARTING"
        RUNNING = "RUNNING"
        PAUSED = "PAUSED"
        RESUMED = "RESUMED"
        STOPPING = "STOPPING"
        STOPPED = "STOPPED"

    def __init__(self) -> None:
        self.started = False
        self.state = self.Lifecycle.CREATED
        self.start_screen = None

    def on_create(self) -> None:
        """Hook invoked when the app is created."""
        self.state = self.Lifecycle.CREATED

    def on_start(self) -> None:
        """Hook invoked when the app starts."""
        self.state = self.Lifecycle.STARTING

    def on_stop(self) -> None:
        """Hook invoked when the app stops."""
        self.state = self.Lifecycle.STOPPED

    def start(self) -> None:
        """Start the application lifecycle."""
        self.state = self.Lifecycle.RUNNING
        self.started = True
