"""Environment detection for Android tooling."""

from __future__ import annotations

import os


class AndroidEnvironment:
    """Detect whether Android development tools are present."""

    def __init__(self) -> None:
        self.android_home = os.environ.get("ANDROID_HOME") or os.environ.get("ANDROID_SDK_ROOT")
        self.adb = "adb" if self._has_command("adb") else None
        self.status = self._detect_status()

    def _has_command(self, name: str) -> bool:
        import shutil

        return shutil.which(name) is not None

    def _detect_status(self) -> str:
        if self.android_home and self.adb:
            return "ready"
        if self.android_home or self.adb:
            return "partial"
        return "missing"
