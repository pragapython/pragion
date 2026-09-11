# Pragion

Pragion is a Python-first Android application framework whose public developer API stays in Python. The project is currently in the Phase 3 UI engine experiment.

## Vision

Pragion aims to provide a Django-like developer experience for Android application development while keeping the public API focused on Python and avoiding Kotlin or Java in application code.

## Current status

This repository includes:

- the Python package foundation
- runtime events and lifecycle support
- a minimal UI model with `Screen`, `Text`, `Button`, `Column`, and `Row`
- a UI tree abstraction and renderer boundary
- CLI support for project creation and Android runtime startup

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
pragion run android
```

## Version

The current version is `0.0.3`.
