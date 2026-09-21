"""Android application build abstraction for the PoC."""

from __future__ import annotations

from pathlib import Path

from .environment import AndroidEnvironment


class AndroidBuildError(RuntimeError):
    """Raised when the Android build environment cannot be used."""


class AndroidBuilder:
    """Build abstraction for a Pragion Android application."""

    def plan(self, project_name: str, mode: str = "debug") -> dict[str, str]:
        """Return a minimal build plan for a project."""
        return {
            "project_name": project_name,
            "mode": mode,
            "output": f"dist/{project_name}-{mode}.apk",
        }

    def build(self, project_path: Path, mode: str = "debug") -> Path:
        """Validate Android tooling and report the future APK output path."""
        environment = AndroidEnvironment()
        if environment.status != "ready":
            raise AndroidBuildError(
                "Android build tools were not detected. Run `pragion doctor` "
                "and configure ANDROID_HOME or ANDROID_SDK_ROOT."
            )

        project_name = project_path.name
        output = project_path / "dist" / f"{project_name}-{mode}.apk"
        raise AndroidBuildError(
            "The native Android builder is not implemented yet; no APK was created. "
            f"Planned output: {output}"
        )
