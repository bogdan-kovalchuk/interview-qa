---
id: py-cpyint-0017
title: "How does `dis` help you check which operations the compiler generates for a small function?"
description: "How does `dis` help you check which operations the compiler generates for a small function?"
track: python
section: cpython-internals
level: middle
type: practical
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

**`dis.dis(func)` prints a table of bytecode instructions: offset, opname (for example `LOAD_FAST`,
`CALL`), argument, and their interpretation – this lets you see exactly which operations the
compiler generated.**[^py314-library-dis] It shows, for example, whether the compiler chose
`LOAD_FAST` over `LOAD_GLOBAL`, how a closure uses `LOAD_DEREF`/`STORE_DEREF`, or whether constant
folding happened. For programmatic analysis, `dis.Bytecode(func)` iterates `Instruction` tuples with
`opcode`, `argval`, `offset`. <span class="warn">Bytecode is a CPython implementation detail and can
change between versions.</span>

## Detailed explanation

`dis` is a built-in module that disassembles the bytecode of a function or code object into a
readable table of instructions, letting you see exactly what the compiler generated instead of
guessing from the source code.[^py314-library-dis]

Calling `dis.dis(func)` prints one line per bytecode instruction: the source line number (for the
first instruction of each line), the byte offset, the `opname` (for example `LOAD_FAST`, `CALL`,
`RETURN_VALUE`), and, where applicable, the argument and its interpretation (`argval`) – for
example the local variable name for `LOAD_FAST`.

This makes compiler decisions visible that you would otherwise have to guess: whether a variable
access compiles to `LOAD_FAST` (local) or `LOAD_GLOBAL` (global); how a closure is implemented –
via `LOAD_DEREF`/`STORE_DEREF` instead of a plain `LOAD_FAST`; or whether constant folding kicked
in, turning `2 + 3` in the source into a single `5` constant in `co_consts` rather than two separate
operations.

An example of disassembling a small function:

```python
def add(a, b):
    return a + b

dis.dis(add)
#   1  RESUME                   0
#   2  LOAD_FAST                0 (a)
#      LOAD_FAST                1 (b)
#      BINARY_OP                0 (+)
#      RETURN_VALUE
```

For programmatic analysis (rather than just reading by eye), `dis.Bytecode(func)` returns an
iterator of `Instruction` objects with `opcode`, `opname`, `arg`, `argval`, `offset` attributes –
this lets you, for example, write a test that checks a certain instruction is absent from a hot
path.

**Practical uses of `dis`:**
- checking whether the compiler inlines a constant expression instead of relying on a guess;
- comparing the bytecode of the same function across two CPython versions to see exactly what
  changed;
- finding unnecessary `LOAD_GLOBAL`s in a hot loop and replacing them with a local name for speed.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
