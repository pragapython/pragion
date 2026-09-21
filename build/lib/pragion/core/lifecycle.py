"""Lifecycle primitives for the Pragion runtime."""

from __future__ import annotations

from enum import Enum


class LifecycleState(str, Enum):
    """Available application lifecycle states."""

    CREATED = "CREATED"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    RESUMED = "RESUMED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
