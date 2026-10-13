---
id: py-modimp-0010
title: "How does a regular package with `__init__.py` differ from a namespace package?"
description: "A regular package is a directory with `__init__.py` in one place; a namespace package has no such file and can merge portions from several directories, but a regular package takes precedence."
track: python
section: modules-and-imports
level: middle
type: comparison
tags: [init-py]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-import
    title: "Python 3.14: Reference/import"
    url: https://docs.python.org/3.14/reference/import.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-importlib
    title: "Python 3.14: Library/importlib"
    url: https://docs.python.org/3.14/library/importlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py-packaging-guide
    title: "Python Packaging User Guide"
    url: https://packaging.python.org/en/latest/tutorials/packaging-projects/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Python Packaging User Guide."
  - source_id: pep-0420
    title: "PEP 420: Implicit Namespace Packages"
    url: https://peps.python.org/pep-0420/
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Regular and namespace packages, namespace package portions, and the precedence of a regular package during search (Python 3.3+)."
  - source_id: py314-reference-import-regular-packages
    title: "Python 3.14: Reference/import (Regular packages)"
    url: https://docs.python.org/3.14/reference/import.html#regular-packages
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Regular package: a directory with __init__.py, which runs on import."
  - source_id: py314-reference-import-namespace-packages
    title: "Python 3.14: Reference/import (Namespace packages)"
    url: https://docs.python.org/3.14/reference/import.html#namespace-packages
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Namespace package portions, which may lie in different directories, and the dynamic __path__ in Python 3.14."
  - source_id: py314-library-importlib-modulespec-origin
    title: "Python 3.14: Library/importlib (ModuleSpec.origin)"
    url: https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.origin
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "origin is None for namespace packages, which have no single file to load from."
---

## Short answer

**A regular package is a directory with an `__init__.py` file; a namespace package has none and can consist of portions in different directories.**[^pep-0420] A regular package's `__init__.py` runs on import.[^py314-reference-import-regular-packages] A regular package with the same name takes precedence, even when it is found later on `sys.path` than the namespace portions.[^pep-0420] A namespace package's `__path__` is a custom iterable, not a list; when the parent path or `sys.path` changes, the next import searches for portions again.[^py314-reference-import-namespace-packages] Its `ModuleSpec.origin` is `None`.[^py314-library-importlib-modulespec-origin]

## Detailed explanation

A regular package and a namespace package are two ways to create a package, and the import system tells them apart while it searches `sys.path`. For each directory `foo`, it checks for `foo/__init__.py`. If that file exists, the regular package is returned at once. If not, but a directory `foo` without `__init__.py` exists, it is recorded as a portion and the search continues. If no regular package is found, a namespace package is created from all the recorded portions.[^pep-0420]

That gives two practical differences. First, a regular package lives in one directory, so its submodules are searched for only there. Second, a namespace package collects submodules from all the portions found on the path, even if they sit in different places in the file system, in zip archives or in other sources.[^py314-reference-import-namespace-packages]

An illustrative example: two directories give one namespace package `shop` (output checked on 3.12, 3.13 and 3.14):

```python
# Layout: site-a/shop/plugins/cart.py and site-b/shop/plugins/search.py; no shop/__init__.py
import sys
sys.path[:0] = ["site-a", "site-b"]
import shop.plugins.cart
import shop.plugins.search
print(shop.__spec__.origin)           # None
print(type(shop.__path__).__name__)   # _NamespacePath
```

`origin` is `None` because a namespace package has no single file that it was loaded from.[^py314-library-importlib-modulespec-origin] The class name `_NamespacePath` is a CPython detail, so code should not depend on it. If `site-a/shop/__init__.py` is added, `shop` becomes a regular package with a single `__path__` (`site-a/shop`), and `import shop.plugins.search` fails with `ModuleNotFoundError`. PEP 420 describes a namespace package as having no `__file__` attribute.[^pep-0420] In CPython 3.12–3.14 the attribute is still present, with the value `None`.

**Common mistakes:**
- adding an empty `__init__.py` to one of the portions and unexpectedly losing subpackages that live in other directories;
- assuming that a namespace package's `__file__` points to a directory: in CPython it is `None`;
- treating a namespace package's `__path__` as an ordinary list that does not change after import: on the next import within the package its portions are recomputed if the parent package's path or `sys.path` has changed.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
