"""UI event integration for the Pragion UI engine."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class UIEvent:
    """A UI event carried through the runtime."""

    name: str
    payload: dict[str, str] | None = None
