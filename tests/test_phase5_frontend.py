from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"


def test_frontend_has_offline_pragion_assets() -> None:
    html = (FRONTEND / "pages" / "ui-gallery.html").read_text(encoding="utf-8")
    css = (FRONTEND / "styles" / "tokens.css").read_text(encoding="utf-8")
    javascript = (FRONTEND / "scripts" / "core.js").read_text(encoding="utf-8")

    assert "pragion-button" in html
    assert "--pragion-color-primary" in css
    assert "window.Pragion" in javascript
    assert "bootstrap" not in html.lower()
    assert "https://" not in html
    assert "dialog.open" in (FRONTEND / "scripts" / "components.js").read_text(encoding="utf-8")


def test_gallery_covers_required_component_families() -> None:
    html = (FRONTEND / "pages" / "ui-gallery.html").read_text(encoding="utf-8")
    for component in (
        "Buttons",
        "Cards",
        "Forms",
        "Tables",
        "Navigation",
        "Dialogs",
        "Bottom Sheets",
        "Tabs",
        "Lists",
        "Charts",
        "Dashboard",
        "Themes",
    ):
        assert f"{component}" in html


def test_frontend_backend_boundaries_are_separate() -> None:
    backend = ROOT / "backend" / "api" / "customer.py"
    frontend_script = FRONTEND / "scripts" / "api.js"

    assert backend.exists()
    assert frontend_script.exists()
    assert "fetch(" in frontend_script.read_text(encoding="utf-8")
    assert "class Customer" in backend.read_text(encoding="utf-8")
