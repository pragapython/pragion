"""Renderer abstraction for the Pragion UI engine."""

from __future__ import annotations

from .tree import UITree, UITreeNode
from .widget import Widget


class Renderer:
    """Base renderer interface for UI trees."""

    def render(self, widget: Widget) -> UITree:
        """Turn a widget into a UI tree."""
        node = UITreeNode(type_name=widget.type_name, id=widget.id, properties={})
        if hasattr(widget, "children"):
            for child in widget.children:
                node.children.append(self.render(child).root)
        return UITree(node)


class AndroidRenderer(Renderer):
    """Android-specific renderer placeholder for the UI PoC."""

    def render(self, widget: Widget) -> UITree:
        return super().render(widget)
