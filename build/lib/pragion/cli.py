"""Command-line interface for Pragion."""

from __future__ import annotations

import argparse
import platform
import sys
from pathlib import Path

from pragion import __version__
from pragion.android import AndroidBuilder, AndroidEnvironment
from pragion.android.builder import AndroidBuildError
from pragion.runtime import Runtime
from pragion.runtime.project import load_application


def _create_project(project_path: str) -> None:
    """Create a minimal Pragion project scaffold."""
    target = Path(project_path)
    if target.exists():
        raise FileExistsError(f"Project directory already exists: {target}")

    target.mkdir(parents=True, exist_ok=False)
    (target / "tests").mkdir()
    project_name = target.name
    package_name = "com.pragion." + project_name.replace("_", "-")

    main_file = target / "main.py"
    main_file.write_text(
        "from pragion import App\nfrom pragion.ui import Button, Column, Screen, Text\n\n\nclass Home(Screen):\n    def build(self):\n        return Column(\n            Text(\"Hello from Pragion\"),\n            Button(\"Click Me\", on_click=self.clicked),\n        )\n\n    def clicked(self) -> None:\n        print(\"Button clicked from Python\")\n\n\nclass HelloApp(App):\n    start = Home\n\n\nif __name__ == \"__main__\":\n    HelloApp().start()\n",
        encoding="utf-8",
    )
    (target / "pragion.toml").write_text(
        f"[project]\nname = \"{project_name}\"\nversion = \"0.0.4\"\n\n[android]\npackage = \"{package_name}\"\nmin_sdk = 26\ntarget_sdk = 35\n\n[application]\nentry = \"main:HelloApp\"\n",
        encoding="utf-8",
    )
    (target / "tests" / "test_app.py").write_text(
        "from main import HelloApp\nfrom pragion.runtime import Runtime\n\n\ndef test_app_starts() -> None:\n    app = HelloApp()\n    Runtime().start(app)\n    assert app.started is True\n",
        encoding="utf-8",
    )


def _doctor() -> str:
    """Collect a minimal environment report."""
    env = AndroidEnvironment()
    return "\n".join(
        [
            "Pragion version: 0.0.4",
            f"Python version: {platform.python_version()}",
            f"Operating system: {platform.system()} {platform.release()}",
            f"Current environment: {env.status}",
            f"Android SDK status: {env.status}",
            f"ADB status: {'available' if env.adb else 'missing'}",
        ]
    )


def _build_android(project_path: Path) -> int:
    """Validate and start the Android build path."""
    try:
        output = AndroidBuilder().build(project_path)
    except AndroidBuildError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Android APK created: {output}")
    return 0


def _run_preview(project_path: Path) -> int:
    """Load the current project and open its local UI preview window."""
    try:
        app = load_application(project_path)
        runtime = Runtime()
        runtime.start(app)
        screen = app.start_screen
        if screen is None:
            raise ValueError("Application does not define a start screen")
        from pragion.runtime.preview import PreviewWindow

        PreviewWindow(screen.build(), runtime).show()
    except (ImportError, RuntimeError) as exc:
        print(f"ERROR: Unable to open Pragion preview: {exc}", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pragion", description="Pragion CLI")
    parser.add_argument("--version", action="store_true", help="Show Pragion version")
    subparsers = parser.add_subparsers(dest="command")

    create_parser = subparsers.add_parser("create", help="Create a new Pragion project")
    create_parser.add_argument("project_name", help="Project directory name")

    subparsers.add_parser("doctor", help="Show environment diagnostics")

    run_parser = subparsers.add_parser("run", help="Run the application")
    run_parser.add_argument(
        "target",
        nargs="?",
        choices=("preview", "android"),
        default="preview",
        help="Target runtime or platform",
    )
    build_parser = subparsers.add_parser("build", help="Build the application")
    build_parser.add_argument("target", choices=("android",), help="Build target")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the Pragion CLI."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.version:
        print(f"Pragion {__version__}")
        return 0

    if args.command == "create":
        try:
            _create_project(args.project_name)
        except FileExistsError as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 1
        print(f"Created project: {args.project_name}")
        return 0

    if args.command == "doctor":
        print(_doctor())
        return 0

    if args.command == "run":
        project_path = Path.cwd()
        if args.target == "preview":
            return _run_preview(project_path)
        if args.target == "android":
            return _build_android(project_path)
        parser.print_help()
        return 0

    if args.command == "build":
        if args.target == "android":
            return _build_android(Path.cwd())
        parser.print_help()
        return 0

    if args.command is None:
        parser.print_help()
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
