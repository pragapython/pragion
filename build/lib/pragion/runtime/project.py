"""Load a Pragion application from a project directory."""

from __future__ import annotations

import importlib
import sys
import tomllib
from pathlib import Path
from typing import Any


def load_application(project_path: Path) -> Any:
    """Load the configured application class from ``pragion.toml``."""
    config_path = project_path / "pragion.toml"
    if not config_path.is_file():
        raise ValueError(f"Pragion project configuration not found: {config_path}")

    with config_path.open("rb") as config_file:
        config = tomllib.load(config_file)
    entry = config.get("application", {}).get("entry")
    if not isinstance(entry, str) or ":" not in entry:
        raise ValueError("Expected [application].entry in pragion.toml, for example main:MyApp")

    module_name, class_name = entry.split(":", 1)
    sys.path.insert(0, str(project_path))
    try:
        module = importlib.import_module(module_name)
    finally:
        sys.path.pop(0)
    application_class = getattr(module, class_name, None)
    if application_class is None:
        raise ValueError(f"Application entry not found: {entry}")
    return application_class()