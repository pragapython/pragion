from __future__ import annotations

from pragion import App
from pragion.runtime import Runtime


def test_runtime_runs_app_and_records_lifecycle_event() -> None:
    class ExampleApp(App):
        def start(self) -> None:
            self.started = True

    runtime = Runtime()
    app = ExampleApp()

    runtime.run(app)

    assert app.started is True
    assert runtime.events
    assert runtime.events[0].name == "app.started"


def test_runtime_dispatches_custom_event() -> None:
    runtime = Runtime()

    runtime.emit("screen.shown", {"screen": "Home"})

    assert runtime.events[-1].name == "screen.shown"
    assert runtime.events[-1].payload == {"screen": "Home"}
