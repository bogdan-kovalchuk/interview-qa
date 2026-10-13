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
updated: 2026-10-13
content_revision: 3
reconciled_with:
  uk: 3
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
  - source_id: packaging-install-requires-vs-requirements
    title: "Python Packaging User Guide: install_requires vs requirements files"
    url: https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/#install-requires-vs-requirements-files
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Official PyPA page: install_requires declares abstract dependencies that pip analyzes at install time; requirements files are lists of pip arguments, often with exact versions, read only by pip install -r."
---

## Short answer

**`pyproject.toml` is standardized configuration: `[build-system]` selects the build backend, while `[project].dependencies` declares install requirements that become distribution metadata.**[^pep621][^packaging-guide] A `requirements.txt` file is conventionally a pip input for installing an environment and may contain pins, hashes, indexes, URLs, constraints, and includes; neither its filename nor pinning is required.[^pip-requirements-format] The files therefore complement rather than replace each other: use `pyproject.toml` for project metadata and supported dependency ranges, and a lock file or fully pinned requirements file is typically used for a reproducible environment.

## Detailed explanation

`pyproject.toml` is a standard file with tables for building and for project metadata. The `[build-system]` table names the build backend and the packages needed to build.[^packaging-guide] The `[project]` table is defined by PEP 621: the `name`, `version` and `dependencies` fields are standardized, and each string in `dependencies` must be a PEP 508 requirement. Such a string becomes a `Requires-Dist` entry in the core metadata of the built distribution.[^pep621] Therefore, when someone installs the project from a wheel or an sdist, pip takes the dependencies from this metadata automatically.[^packaging-install-requires-vs-requirements]

`requirements.txt` has a different role. It is a list of arguments for `pip install`: each line is a requirement, an option, or a reference to another file. Pip reads such a file only when it is passed through `-r` (for example `pip install -r` or `pip download -r`), not when a project is installed from its metadata.[^packaging-install-requires-vs-requirements] The format allows exact pins, `--hash`, `--index-url`, `-r` for nested files and `-c` for constraints.[^pip-requirements-format] At the same time, a plain line without a version, such as `pytest`, is also valid, so pinning versions is not required in this format.[^pip-requirements-format]

The typical difference shows up in the example. A library declares a range in `pyproject.toml`, while a concrete environment build pins a version in `requirements.txt`:

```toml
# pyproject.toml: the project declares a range it supports
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "demo-app"
version = "0.1.0"
dependencies = ["httpx>=0.27,<1"]   # any httpx from 0.27 up to, not including, 1.0
```

```text
# requirements.txt: exact versions for one tested environment
httpx==0.28.1
```

A real requirements file usually contains a complete list of pinned versions, including the transitive dependencies of httpx that the example omits. This is how repeatable installations are achieved.[^packaging-install-requires-vs-requirements] For the library itself, by contrast, the recommended practice is to give a range with a minimum and, if needed, an upper bound. An exact pin in `dependencies` forces consumers to refuse upgrades, so it is not considered good practice.[^packaging-install-requires-vs-requirements]

**Common mistakes:**
- putting exact versions in `[project].dependencies`, so that consumers of the library cannot upgrade the dependency;
- assuming that `requirements.txt` is part of the build metadata: the project's installer does not read it;
- assuming that the file name matters: pip accepts any name in `-r`, because `requirements.txt` is only the usual name.[^pip-requirements-format]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
