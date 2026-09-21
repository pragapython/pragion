# WebView Architecture

Pragion targets a trusted, packaged WebView surface:

```text
Packaged HTML/CSS/JS
  ↓
Android WebView
  ↓
Pragion protocol adapter
  ↓
Python runtime
```

Core UI assets are local and do not depend on a CDN. Android packaging is not implemented in 0.0.5; this document defines the boundary for a later native build bridge.
