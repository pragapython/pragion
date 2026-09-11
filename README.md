# Pragion

Pragion is a Python-first Android application framework foundation for the 0.0.1 release.

## Vision

Pragion aims to provide a Django-like, Python-native developer experience for Android application development while keeping the public API focused on Python and avoiding Kotlin or Java in application code.

## Current status

This repository is the Phase 1 foundation for Pragion. It includes:

- Python package scaffolding under src/pragion
- version metadata and importable App base class
- CLI with `--version`, `create`, and `doctor` commands
- basic tests for the foundation layer
- CI workflow for lint and testing

## Quick start

```bash
python -m pip install -e '.[dev]'
pragion --version
pragion create hello
cd hello
python main.py
```

## Planned phases

The project is intentionally scoped to the 0.0.1 foundation and will proceed incrementally toward runtime and Android integration in later phases.
