from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pragion
from pragion import App


def test_version() -> None:
    assert pragion.__version__ == "0.0.4"


def test_app_can_be_subclassed() -> None:
    class ExampleApp(App):
        def start(self) -> None:
            self.started = True

    app = ExampleApp()
    assert callable(app.start)
    app.start()
    assert app.started is True


def test_cli_version() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "-m", "pragion", "--version"],
        capture_output=True,
        text=True,
        cwd=str(repo_root),
        check=False,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "Pragion 0.0.4"


def test_project_generator(tmp_path: Path) -> None:
    project_dir = tmp_path / "hello"
    result = subprocess.run(
        [sys.executable, "-m", "pragion", "create", str(project_dir)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert (project_dir / "main.py").exists()
    assert (project_dir / "pragion.toml").exists()
    assert (project_dir / "tests").is_dir()
    assert (project_dir / "tests" / "test_app.py").exists()


def test_doctor() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "-m", "pragion", "doctor"],
        capture_output=True,
        text=True,
        cwd=str(repo_root),
        check=False,
    )
    assert result.returncode == 0
    assert "Pragion version" in result.stdout
    assert "Python version" in result.stdout
    assert "Operating system" in result.stdout
