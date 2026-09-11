# Android Setup and Runtime PoC

## Current experiment

This release is an early runtime proof of concept for Pragion. It does not yet produce a complete Android APK, but it defines the architecture needed to get there.

## Requirements

- Python 3.12+
- `pragion` installed in editable mode
- optional Android SDK tools for future runtime checks

## Commands

```bash
pragion --version
pragion create hello
cd hello
pragion run android
pragion doctor
```

## Important note

The developer experience remains Python-first. The Android toolchain is internal to the framework and is not part of the public application API.
