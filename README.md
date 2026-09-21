# Pragion

Pragion is a Python-first Android application framework whose public developer API stays in Python. The project is currently in the 0.0.5 Pragion UI design-system phase.

## Vision

Pragion aims to provide a Django-like developer experience for Android application development while keeping the public API focused on Python and avoiding Kotlin or Java in application code.

## Current status

This repository includes:

- the Python package foundation
- runtime events and lifecycle support
- a minimal UI model with `Screen`, `Text`, `Button`, `Column`, and `Row`
- a UI tree abstraction and renderer boundary
- a local desktop preview for the supported UI widgets
- CLI support for project creation, preview, and Android build validation
- an offline HTML/CSS/JavaScript Pragion UI gallery
- explicit backend/frontend separation and a JSON UI protocol boundary

## Quick example

```python
from pragion import App
from pragion.ui import Button, Column, Screen, Text


class Home(Screen):
    def build(self):
        return Column(
            Text("Hello from Pragion"),
            Button("Click Me", on_click=self.clicked),
        )

    def clicked(self) -> None:
        print("Button clicked from Python")


class MyApp(App):
    start = Home
```

## Quick start

```bash
python -m pip install -e '.[dev]'
pragion --version
pragion create hello
cd hello
pragion run
```

`pragion run` opens a local preview window on a desktop session. `pragion build android` checks the Android toolchain; native APK generation is not implemented yet.

To inspect the complete first-party UI system:

```bash
pragion ui gallery
```

The gallery is local and offline at `frontend/pages/ui-gallery.html`. The example backend boundary lives in `backend/api/customer.py` and is consumed through JSON by `frontend/scripts/api.js`.

## Version

The current version is `0.0.5`.
