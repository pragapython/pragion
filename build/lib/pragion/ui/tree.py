"""UI tree model for the Pragion UI engine."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class UITreeNode:
    """A node in the internal UI tree."""

    type_name: str
    id: str
    parent: UITreeNode | None = None
    children: list[UITreeNode] = field(default_factory=list)
    properties: dict[str, Any] = field(default_factory=dict)


class UITree:
    """Tree wrapper for a rendered screen."""

    def __init__(self, root: UITreeNode) -> None:
        self.root = root
        self.type_name = root.type_name
        self.id = root.id
        self.children = root.children
        self.properties = root.properties
