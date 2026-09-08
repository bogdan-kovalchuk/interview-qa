---
id: py-pkgenv-0001
title: "What is the difference between requirements.txt and pyproject.toml for managing Python project dependencies?"
description: "pyproject.toml declares standardized project and build metadata; requirements.txt conventionally contains pip installation inputs for an environment, and the two files can be used together."
track: python
section: packaging-and-environments
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-08
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: pep621
    title: "PEP 621: Storing project metadata in pyproject.toml"
    url: https://peps.python.org/pep-0621/
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "PEP that standardized pyproject.toml for project metadata."
  - source_id: packaging-guide
    title: "Python Packaging User Guide: Writing pyproject.toml"
    url: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Official Python packaging documentation."
  - source_id: pip-requirements-format
    title: "pip documentation: Requirements File Format"
    url: https://pip.pypa.io/en/stable/reference/requirements-file-format/
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Official pip specification of requirements file syntax and scope."
---

## Short answer

**`pyproject.toml` is standardized configuration: `[build-system]` selects the build backend, while `[project].dependencies` declares install requirements that become distribution metadata.**[^pep621][^packaging-guide] A `requirements.txt` file is conventionally a pip input for installing an environment and may contain pins, hashes, indexes, URLs, constraints, and includes; neither its filename nor pinning is required.[^pip-requirements-format] The files therefore complement rather than replace each other: use `pyproject.toml` for project metadata and supported dependency ranges, and a lock file or fully pinned requirements file when a reproducible environment is needed.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
