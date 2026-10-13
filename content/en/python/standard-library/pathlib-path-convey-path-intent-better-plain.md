---
id: py-stdlib-0009
title: "Why does `pathlib.Path` convey path intent better than a plain string?"
description: "Why does `pathlib.Path` convey path intent better than a plain string?"
track: python
section: standard-library
level: middle
type: comparison
tags: [pathlib-path]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-pathlib-pure-paths
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html#pure-paths
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, Pure paths section: pure paths do not access the filesystem; path properties (name, suffix, parent)."
  - source_id: py314-library-pathlib-concrete-paths
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html#concrete-paths
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, Concrete paths section: Path creates a PosixPath or WindowsPath depending on the OS; concrete paths have methods that make system calls."
  - source_id: py314-library-pathlib-operators
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html#operators
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, Operators section: the slash operator creates child paths."
  - source_id: py314-library-pathlib-general-properties
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html#general-properties
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, General properties section: paths are immutable and hashable; comparison follows the case-folding rules of the OS flavour."
---

## Short answer

**`Path` is an object abstraction of a path that separates path operations from filesystem access, whereas a string is just text.**[^py314-library-pathlib-pure-paths] `Path` becomes a `PosixPath` or a `WindowsPath` depending on the OS; the `/` operator creates child paths, and `exists()` and `is_file()` access the filesystem.[^py314-library-pathlib-concrete-paths][^py314-library-pathlib-operators] Paths are immutable and hashable, so they can be used as dict keys.[^py314-library-pathlib-general-properties]

## Detailed explanation

A string holds a path as text, so separators, suffixes, and joining parts remain the developer's job. `pathlib` has two levels. Pure paths (`PurePath`, `PurePosixPath`, `PureWindowsPath`) only compute over a path and do not access the filesystem. A concrete `Path` has the same operations and adds methods that make system calls.[^py314-library-pathlib-pure-paths][^py314-library-pathlib-concrete-paths]

The example builds a path with `/` and shows its parts. The output shown is for POSIX:

```python
from pathlib import Path, PureWindowsPath

p = Path("data") / "reports" / "2026.csv"
print(p)                                       # data/reports/2026.csv
print(p.suffix, p.name, p.parent)              # .csv 2026.csv data/reports
print(p.with_suffix(".json"))                  # data/reports/2026.json
print(PureWindowsPath("C:/logs") / "app.log")  # C:\logs\app.log on any OS
print({p: "report"}[Path("data/reports/2026.csv")])  # report
p.endswith(".csv")                             # AttributeError: 'PosixPath' object has no attribute 'endswith'
```

The `/` operator creates a child path.[^py314-library-pathlib-operators] The properties `name`, `suffix`, and `parent` return parts of the path.[^py314-library-pathlib-pure-paths] `with_suffix()` returns a new object, because paths are immutable.[^py314-library-pathlib-general-properties] Being hashable means a path can be used as a dict key, as in the example above.

Comparison also depends on the OS: `PurePosixPath('foo') == PurePosixPath('FOO')` gives `False`, while `PureWindowsPath('foo') == PureWindowsPath('FOO')` gives `True`. So `Path` conveys intent, but case and separator rules remain those of the particular system.[^py314-library-pathlib-general-properties]

**Common mistakes:**
- treating a `Path` as a string: `p.endswith(".csv")` raises `AttributeError`, and an API that expects a str needs `str(p)` or `os.fspath(p)`;
- assuming a `Path` never touches the disk: `exists()`, `is_file()`, and `mkdir()` make system calls, unlike `PurePath`;
- comparing paths as strings: `PureWindowsPath` ignores case, while `PurePosixPath` does not.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
