from __future__ import annotations

from pragion import App
from pragion.android import AndroidBuilder, AndroidEnvironment
from pragion.runtime import Event, Runtime
from pragion.ui import Button, Screen, Text, Widget


def test_app_has_lifecycle_states() -> None:
    assert App.Lifecycle.CREATED.value == "CREATED"
    assert App.Lifecycle.RUNNING.value == "RUNNING"
    assert App.Lifecycle.STOPPED.value == "STOPPED"


def test_screen_and_widgets_are_created() -> None:
    class Home(Screen):
        def build(self):
            return [Text("Hello from Pragion"), Button("Click Me")]

    home = Home()
    widgets = home.build()
    assert len(widgets) == 2
    assert isinstance(widgets[0], Text)
    assert isinstance(widgets[1], Button)
    assert isinstance(home, Widget)


def test_runtime_dispatches_events() -> None:
    runtime = Runtime()
    runtime.dispatch(Event(name="button_click", payload={"id": "home_button"}))

    assert runtime.events[-1].name == "button_click"
    assert runtime.events[-1].payload == {"id": "home_button"}


def test_android_environment_reports_status() -> None:
    env = AndroidEnvironment()
    assert env.status in {"ready", "missing", "partial"}


def test_android_builder_has_debug_build_method() -> None:
    builder = AndroidBuilder()
    plan = builder.plan(project_name="hello")
    assert plan["project_name"] == "hello"
    assert plan["mode"] == "debug"
