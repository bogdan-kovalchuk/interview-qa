---
id: py-cpyint-0003
title: "Why should `dis` output be treated as an implementation detail of a specific CPython version rather than a language contract?"
description: "Why should `dis` output be treated as an implementation detail of a specific CPython version rather than a language contract?"
track: python
section: cpython-internals
level: senior
type: pitfall
tags: [dis]
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
  - source_id: py314-library-dis
    title: "Python 3.14: Library/dis"
    url: https://docs.python.org/3.14/library/dis.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-gc
    title: "Python 3.14: Library/gc"
    url: https://docs.python.org/3.14/library/gc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-c-api-memory
    title: "Python 3.14: C Api/memory"
    url: https://docs.python.org/3.14/c-api/memory.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-sys
    title: "Python 3.14: Library/sys"
    url: https://docs.python.org/3.14/library/sys.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
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
  - source_id: py314-reference-datamodel-traceback-objects
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#traceback-objects
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L3-L26
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Bytecode is a CPython implementation detail: the documentation explicitly states that
instructions can be added, removed, or changed between versions without warning.**[^py314-library-dis]
Opcodes, their encoding, and their semantics are not guaranteed even between CPython minor releases,
and other implementations (PyPy, MicroPython) have their own bytecode. Code that relies on specific
opcodes or their order becomes non-portable and fragile across upgrades.

## Detailed explanation

The official Python documentation explicitly calls bytecode an implementation detail: the set of
opcodes, their encoding, and even the number of arguments can change between any CPython versions –
including minor releases – without a backward-compatibility guarantee.[^py314-library-dis]

This is not a hypothetical risk: for example, 3.11 introduced `RESUME` at the start of every code
object, and several call opcodes (`CALL_FUNCTION`, `CALL_FUNCTION_KW`, `CALL_METHOD`) were merged
into a single `CALL` with shared stack setup. Code written against one version's bytecode can, after
an interpreter upgrade, either fail with an error or – worse – silently start analyzing the wrong
instructions.

The language contract is the syntax and semantics described in the reference documentation, which
change through a PEP process with a deprecation period. Bytecode goes through no such process: it is
optimized for a specific version of the eval loop, and an opcode change is not considered a breaking
change to the language, even if code built on top of `dis` breaks.

```python
# CPython 3.10 and earlier
CALL_FUNCTION            2

# CPython 3.11+: unified into CALL with a preceding PUSH_NULL/precall setup
CALL                      2
```

Other Python implementations confirm that bytecode is not part of the language: PyPy has its own
opcode set for its interpreter, and MicroPython generates an even more compact format for
constrained memory. Both execute the same Python code correctly while sharing nothing with
CPython's bytecode.

**Practical consequences for code that reads bytecode:**
- any check or tool based on specific opcode names must be pinned to an interpreter version and
  re-verified after an upgrade;
- do not store or cache a `code object` from one CPython patch release to run it on another – the
  `.pyc` format is versioned too;
- build performance or coverage analysis on `sys.settrace`/`sys.monitoring` rather than on parsing
  specific opcodes.

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
