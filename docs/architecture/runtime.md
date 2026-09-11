# Pragion Runtime Architecture

## Overview

Pragion is designed as a Python-first application framework that runs through a thin runtime layer before bridging to Android-native execution. The runtime is intentionally small at this stage and exists to establish the architecture needed for later Android integration.

## Flow

```text
Python application
  ↓
Pragion bootstrap
  ↓
Pragion runtime
  ↓
Application lifecycle
  ↓
Event system
  ↓
Screen / UI layer
```

## Layers

### 1. Python application

The developer writes application code in Python and interacts with Pragion APIs rather than Android SDKs directly.

### 2. Pragion bootstrap

The bootstrap layer initializes configuration, loads the application class, and prepares the runtime environment.

### 3. Pragion runtime

The runtime manages lifecycle events, dispatches application callbacks, and keeps platform-specific complexity isolated behind a stable Python interface.

### 4. Application lifecycle

The application lifecycle is simple and explicit:

- create app instance
- initialize runtime
- run app
- emit `app.started`
- allow screen or UI layer interaction

### 5. Event system

Events are lightweight messages that carry a name and payload. They let the runtime and future UI layers communicate without hard-coding platform-specific behavior into the Python application layer.

### 6. Screen and UI layer

The UI layer sits above the runtime and is responsible for rendering screens and responding to user interaction events.

## Goals for 0.0.2

This architecture defines the boundary for the first runtime PoC:

- Python app code remains the developer-facing API
- runtime handles lifecycle and event dispatch
- Android-specific code remains isolated and future-facing
- no full APK generation yet

## Example

```python
from pragion import App


class MyApp(App):
    def start(self) -> None:
        print("Hello from Pragion")
```

The runtime eventually calls `start()` as part of the application lifecycle.
