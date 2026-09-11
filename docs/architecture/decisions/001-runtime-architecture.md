# 001: Runtime architecture

## Context

Pragion must keep the public developer API Python-first while eventually bridging to Android execution. The framework needs a minimal runtime layer before any Android build integration is attempted.

## Decision

Use a small runtime object that owns lifecycle state, dispatches events, and isolates Android-specific integration behind internal modules.

## Reason

This keeps the architecture testable, simple, and extensible while remaining compatible with the long-term design of a Python-centric framework.

## Alternatives considered

- full Android build logic in the CLI immediately
- exposing Android SDK details to application developers
- designing a large event bus before proving runtime flow

## Advantages

- minimal surface area
- testable in Python-only environment
- clear separation between public API and Android internals

## Limitations

- not yet connected to a real Android application runtime
- not yet capable of producing end-user APKs
- UI rendering is intentionally minimal

## Future impact

This architecture gives a stable base for later Android runtime bridging, UI work, and build pipeline additions.
