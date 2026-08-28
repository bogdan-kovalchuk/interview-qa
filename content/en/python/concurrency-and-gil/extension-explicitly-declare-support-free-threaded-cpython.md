---
id: py-gil-0011
title: "How does a C extension explicitly declare support for free-threaded CPython 3.14, and what can happen when an incompatible extension is imported?"
description: "How does a C extension explicitly declare support for free-threaded CPython 3.14, and what can happen when an incompatible extension is imported?"
track: python
section: concurrency-and-gil
level: senior
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython free-threaded build"
    version: "3.14"
anki:
  export: true
sources:
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-multiprocessing
    title: "Python 3.14: Library/multiprocessing"
    url: https://docs.python.org/3.14/library/multiprocessing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-concurrent-futures
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-free-threading-extensions
    title: "Python 3.14: Howto/free Threading Extensions"
    url: https://docs.python.org/3.14/howto/free-threading-extensions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**A C extension declares free-threaded build support through the `Py_mod_gil` slot with the value
`Py_MOD_GIL_NOT_USED` (multi-phase init) or by calling
`PyUnstable_Module_SetGIL(module, Py_MOD_GIL_NOT_USED)` (single-phase init).**[^py314-library-threading]
<span class="warn">If the extension does not declare support:</span> import raises a warning and the
GIL is automatically re-enabled, negating the benefits of the free-threaded build. Conditional
compilation uses the `Py_GIL_DISABLED` macro.

## Detailed explanation

A free-threaded CPython build requires every C extension to explicitly state that it is safe to run
without the GIL; without that declaration the extension is treated as incompatible, and CPython
falls back to re-enabling the GIL by default.[^py314-howto-free-threading-extensions]

How you declare it depends on the extension's init style. For multi-phase init (PEP 489, using
`Py_mod_exec` slots), you add a separate `Py_mod_gil` slot with the value `Py_MOD_GIL_NOT_USED` in
the `PyModuleDef_Slot` array. For the older single-phase init, where the module is created directly
via `PyModule_Create`, the same effect comes from calling
`PyUnstable_Module_SetGIL(module, Py_MOD_GIL_NOT_USED)` inside the `PyInit_*` function right after
the module object is created.

Example of declaring free-threaded support in multi-phase init:

```c
static PyModuleDef_Slot module_slots[] = {
    {Py_mod_exec, module_exec},
    {Py_mod_gil, Py_MOD_GIL_NOT_USED},
    {0, NULL},
};
```

If an extension contains neither declaration, importing it on a free-threaded build raises a
`RuntimeWarning` and automatically re-enables the GIL for the whole process, even if the extension
happens to be thread-safe. This is a conservative "unsafe by default" policy: CPython does not try
to guess an extension's safety, it relies on an explicit opt-in from the author.[^py314-howto-free-threading-python]

Conditional code for the free-threaded build uses the `Py_GIL_DISABLED` macro, which is defined only
in that build. It lets you wrap sections that need extra synchronization (critical sections, atomic
operations) in `#ifdef Py_GIL_DISABLED` instead of duplicating the whole file for both
configurations.

**Common mistakes:**
- declaring `Py_MOD_GIL_NOT_USED` without actually checking the thread safety of internal C
  structures and caches;
- forgetting that the declaration is a promise made by the extension author, not an automatic check
  performed by CPython;
- confusing `Py_mod_gil` (a per-module slot) with the build-wide compilation flag `Py_GIL_DISABLED`
  (a per-build macro).

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
