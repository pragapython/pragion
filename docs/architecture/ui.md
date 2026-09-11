# Pragion UI Architecture

## Goal

The first UI abstraction is intentionally tiny. It is designed to prove the flow from Python-defined UI to a runtime model and then to Android rendering. The public API stays Python-first and does not require the developer to write Kotlin, Java, or XML.

## Core concepts

- `Widget`: base class for all user-interface elements
- `Text`: simple text widget
- `Button`: clickable widget with an optional handler
- `Screen`: container for widgets displayed in a window or activity

## Design

The runtime PoC describes the shape of the UI model rather than a full rendering engine. The architecture separates:

1. Python declaration
2. Pragion UI model
3. Android adapter layer
4. display surface

This makes it possible to evolve the rendering engine later without changing the public application API.

## Current limitations

This is not a full widget system. It does not yet include layout containers, styles, list rendering, navigation, or animation. Those features belong to later phases.
