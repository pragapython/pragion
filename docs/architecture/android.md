# Pragion Android Bridge Architecture

## Goal

The Android bridge is intentionally isolated from the public Python API. The developer writes Python and the framework handles the underlying Android integration internally.

## Main responsibilities

- detect Android SDK and tooling
- create a debug build plan
- prepare app metadata
- provide a runtime entry point for Android execution
- forward Android events into the Pragion runtime

## Current status

This is a conceptual bridge for the runtime PoC. It does not yet generate a real Android APK or install onto a device. The focus is on proving the architecture and defining the boundary between Python runtime logic and Android implementation details.

## Future work

- generate native Android project templates
- install onto emulator/device
- bridge Android UI events into Python callbacks
- compile debug APK for the first real hello-world app
