"""Android application build abstraction for the PoC."""

from __future__ import annotations


class AndroidBuilder:
    """Minimal builder abstraction for a debug Android app."""

    def plan(self, project_name: str, mode: str = "debug") -> dict[str, str]:
        """Return a minimal build plan for a project."""
        return {
            "project_name": project_name,
            "mode": mode,
            "output": f"dist/{project_name}-{mode}.apk",
        }
