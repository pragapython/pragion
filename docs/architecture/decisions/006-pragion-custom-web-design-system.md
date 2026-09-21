# 006: Pragion custom web design system

## Context

Pragion needs a Python-owned application layer and a maintainable UI layer that can run offline inside a future Android WebView.

## Decision

Pragion UI will use standard HTML, first-party CSS, and focused JavaScript modules. Bootstrap is rejected as a runtime dependency. Flutter and a custom native renderer are also not the selected UI implementation for this phase.

## Reason

This preserves a clear backend/frontend boundary, keeps assets packageable, supports WebView execution, and lets Pragion own its public component vocabulary and visual identity.

## Limitations

The 0.0.5 system is a design-system foundation, not a complete WebView-to-Python bridge or native APK builder.
