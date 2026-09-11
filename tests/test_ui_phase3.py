from __future__ import annotations

from pragion.runtime import Runtime
from pragion.ui import Button, Column, Row, Screen, Text, Widget


def test_widget_has_basics() -> None:
    widget = Widget(id="w1")
    assert widget.id == "w1"
    assert widget.visible is True
    assert widget.enabled is True
    assert widget.parent is None


def test_text_and_button_creation() -> None:
    label = Text("Hello from Pragion")
    button = Button("Click Me")

    assert label.text == "Hello from Pragion"
    assert button.text == "Click Me"
    assert button.visible is True


def test_column_and_row_keep_order() -> None:
    column = Column(Text("One"), Text("Two"))
    row = Row(Text("A"), Button("B"))

    assert [child.text for child in column.children] == ["One", "Two"]
    assert [child.text for child in row.children] == ["A", "B"]


def test_screen_build_returns_widgets() -> None:
    class Home(Screen):
        def build(self):
            return Column(Text("Hello"), Button("Click"))

    screen = Home()
    screen_widgets = screen.build()
    assert len(screen_widgets.children) == 2
    assert screen_widgets.children[0].text == "Hello"


def test_button_callback_is_dispatched() -> None:
    runtime = Runtime()
    calls: list[str] = []

    def clicked() -> None:
        calls.append("clicked")

    button = Button("Click Me", on_click=clicked)
    button.dispatch_click(runtime)

    assert calls == ["clicked"]
    assert runtime.events[-1].name == "button_click"
    assert runtime.events[-1].payload == {"widget_id": button.id}


def test_ui_tree_builds_from_screen() -> None:
    class Home(Screen):
        def build(self):
            return Column(Text("Hello"), Button("Click Me"))

    screen = Home()
    tree = screen.ui_tree()
    assert tree.type_name == "Column"
    assert tree.children[0].type_name == "Text"
    assert tree.children[1].type_name == "Button"
