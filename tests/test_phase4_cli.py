from __future__ import annotations

from pathlib import Path

from pragion.cli import _build_parser, _create_project
from pragion.runtime import Runtime
from pragion.runtime.preview import PreviewWindow
from pragion.ui import Text


def test_build_android_command_is_registered() -> None:
    parser = _build_parser()
    args = parser.parse_args(["build", "android"])

    assert args.command == "build"
    assert args.target == "android"


def test_create_project_uses_phase4_ui_entry(tmp_path: Path) -> None:
    project = tmp_path / "myfirstapp"
    _create_project(str(project))

    main_source = (project / "main.py").read_text(encoding="utf-8")
    config = (project / "pragion.toml").read_text(encoding="utf-8")

    assert "Column" in main_source
    assert "Button(\"Click Me\", on_click=self.clicked)" in main_source
    assert 'version = "0.0.4"' in config


def test_run_without_target_defaults_to_preview() -> None:
    parser = _build_parser()
    args = parser.parse_args(["run"])

    assert args.command == "run"
    assert args.target == "preview"


def test_preview_reports_missing_desktop_display(monkeypatch) -> None:
    monkeypatch.delenv("DISPLAY", raising=False)

    try:
        PreviewWindow(Text("Hello"), Runtime())
    except RuntimeError as exc:
        assert "No desktop display is available" in str(exc)
