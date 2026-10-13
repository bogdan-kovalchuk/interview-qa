---
id: py-modimp-0004
title: "How can violating the import protocol or manually editing `sys.modules` lead to two module objects for the same source file?"
description: "How can violating the import protocol or manually editing `sys.modules` lead to two module objects for the same source file?"
track: python
section: modules-and-imports
level: senior
type: pitfall
tags: [sys-modules]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: null
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
  - source_id: py314-reference-import-module-cache
    title: "Python 3.14: Reference/import, The module cache"
    url: https://docs.python.org/3.14/reference/import.html#the-module-cache
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Section “The module cache” of the official Python 3.14 documentation: sys.modules is keyed by module name; after a key is deleted and the module is imported again, the two module objects are not the same if a reference to the old one is kept."
---

## Short answer

**The same file can be imported under different full names, and then `sys.modules` holds two different module objects for one source file.**[^py314-reference-import-module-cache] <span class="warn">This is dangerous when the module keeps state (a singleton, a cache, a registry) or defines classes that are checked by type: each copy has its own state, and `isinstance` and `except` checks against classes from different copies do not match.</span> The key in `sys.modules` is the full name, not the file path, so `pkg.registry` and `registry` are different modules to Python.[^py314-reference-import-module-cache]

## Detailed explanation

The key in `sys.modules` is the full module name, not the path to the file.[^py314-reference-import-module-cache] So one source file imported under two names produces two module objects: each name has its own cache entry, and each load executes the file separately. Identical entries in `sys.path` do not create a duplicate by themselves, because a repeated import of the same name finds its cache entry.

The example creates a package `pkg` with a stateful module `registry`. The package folder is added to `sys.path` next to its parent, so the same file is reachable both as `pkg.registry` and as `registry`:

```python
import sys
import tempfile
from pathlib import Path

# A throwaway package on disk: pkg/registry.py holds state and a class.
root = Path(tempfile.mkdtemp())
(root / 'pkg').mkdir()
(root / 'pkg' / '__init__.py').write_text('')
(root / 'pkg' / 'registry.py').write_text("class Plugin: pass\nREGISTRY = []\n")
sys.path.insert(0, str(root))
sys.path.insert(0, str(root / 'pkg'))  # the same folder is now also a top-level path

import pkg.registry as via_package   # cached as 'pkg.registry'
import registry as via_flat          # same source file, different name

print(via_package is via_flat)                          # False: two module objects
print(via_package.__file__ == via_flat.__file__)        # True: same source file
print(isinstance(via_flat.Plugin(), via_package.Plugin))  # False: two class objects

# Manually dropping a cache entry and importing again also gives a second object.
first = via_package
del sys.modules['pkg.registry']
import pkg.registry as second
print(first is second)                                  # False
print(first.REGISTRY is second.REGISTRY)                # False: state is not shared
```

In the output, `via_package is via_flat` is `False`, while `__file__` matches. A `Plugin` from one copy is not an instance of the other copy's `Plugin`, because `class` runs twice and creates two classes. The state is duplicated too, since each copy has its own `REGISTRY`.

The manual route gives the same result: after `del sys.modules[...]`, the old reference points to a different object with its own state. The documentation says directly that two such objects will not be the same.[^py314-reference-import-module-cache]

A duplicate is harmful when the module keeps state, defines classes that are checked by type (`isinstance`, `except`), or has side effects at import. Even without state, classes from different copies do not match. Safeguards: one full import name per file, no package folder in `sys.path`, and no hand-editing of `sys.modules`.

**Common mistakes:**
- assuming that identical `__file__` values mean one module object (the cache key is the name);
- adding a package folder to `sys.path` to "simplify" imports and getting a second copy of the module with its own state;
- deleting an entry from `sys.modules` to reset state without noticing that old references still hold the previous state.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
