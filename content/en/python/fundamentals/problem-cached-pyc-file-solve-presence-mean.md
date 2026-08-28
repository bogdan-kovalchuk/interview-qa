---
id: py-fund-0003
title: "What problem does the cached `.pyc` file solve, and why does its presence not mean the Python code was compiled to native machine code?"
description: "What problem does the cached `.pyc` file solve, and why does its presence not mean the Python code was compiled to native machine code?"
track: python
section: fundamentals
level: middle
type: mechanism
tags: [pyc]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-reference-executionmodel
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-faq-general
    title: "Python 3.14: Faq/general"
    url: https://docs.python.org/3.14/faq/general.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L382-L406
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**A `.pyc` lets the compiled bytecode of an unchanged imported module be reused instead of spending time compiling the source again.**[^py314-reference-executionmodel] It holds bytecode for the Python VM, not processor instructions. The bytecode format is a CPython implementation detail and may change between versions.

## Detailed explanation

A `.pyc` is a cache of the result of compilation, not a "compiled program". It holds a marshalled
code object with bytecode for the Python virtual machine, not machine instructions for the
processor.[^py314-reference-executionmodel]

The problem it solves is narrow: remove the repeated parsing and compilation on every import.
Compilation takes noticeable time on a large codebase, and for an unchanged file the result is
always the same, so it is worth storing. The files live in `__pycache__` next to the module, named
with the implementation tag and the version.

Cache validity is checked on every import. By default the `.pyc` header records the modification
time and size of the source file; if they do not match what is on disk, the cache is ignored and the
module is recompiled.

```python
# my_module.py compiled once, then reused on every later import:
__pycache__/my_module.cpython-314.pyc

# the tag says which implementation and which version wrote it -
# a 3.13 interpreter will not read a 3.14 file, it will recompile
```

Three things the presence of a `.pyc` does **not** mean. It does not speed up the executing code -
the bytecode is the same, only the compilation is saved. It is not a way to hide the source:
bytecode disassembles. And it does not make code portable between Python versions, because the
bytecode format is an internal CPython detail that changes between releases.[^py314-faq-general]

**Worth knowing about the cache's behaviour:**
- the cache is written only for **imported** modules; a script run as `python script.py` is not
  cached, because it is compiled exactly once per process;
- if the directory is not writable, the import still works - just without a cache, more slowly;
- the mtime check is unreliable in deployments where files get identical timestamps; for that there
  is a hash-based mode which compares a hash of the source file;
- deleting `__pycache__` is safe: the next import recreates the cache.

The practical conclusion for an interview: a `.pyc` is a CPython implementation detail that saves
import time. Building any application logic on its format, its location or the mere fact of its
existence is a bad idea.[^py314-reference-datamodel]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
