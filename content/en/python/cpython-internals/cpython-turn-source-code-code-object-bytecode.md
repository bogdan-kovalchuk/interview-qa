---
id: py-cpyint-0001
title: "How does CPython turn source code into a code object and bytecode before execution?"
description: "How does CPython turn source code into a code object and bytecode before execution?"
track: python
section: cpython-internals
level: middle
type: mechanism
tags: []
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

**CPython compiles source code into a code object that contains bytecode, and then the interpreter
executes that bytecode instruction by instruction.**[^py314-library-dis] The process goes through
the stages parsing -> AST -> code object (via the built-in `compile()`). The code object stores
`co_code` (bytecode), `co_consts`, `co_names`, `co_varnames`, and other static data. On import, the
compiled bytecode can be cached in `.pyc` files.

## Detailed explanation

Compilation in CPython is a multi-stage process that turns source code text into an executable
`code object` before the interpreter executes even a single instruction.[^py314-library-dis]

First, the tokenizer and parser build an abstract syntax tree (AST) from the program text. The
compiler walks that AST and generates a `code object` – an object that holds `bytecode` (a sequence
of low-level instructions for the CPython eval loop) together with the static data needed to
execute it. The compiler itself is written in C and is not directly accessible from pure Python, but
the built-in `compile()` function performs the same steps and returns a ready `code object`.

The `code object` stores several separate fields: `co_code` – the bytecode bytes; `co_consts` – a
tuple of literals and nested `code object`s (for example, function bodies); `co_names` – the names
of global variables and attributes; `co_varnames` – the names of local variables. The interpreter
reads these fields during execution rather than re-parsing the source.

An example of manually compiling and inspecting bytecode:

```python
src = "x = 1 + 2"
code = compile(src, "<string>", "exec")
print(code.co_consts)  # (1, 2, 3, None)
dis.dis(code)
```

When a module is imported (rather than run as `__main__`), CPython caches the compiled
`code object` in a `.pyc` file under `__pycache__/`, serializing it via `marshal`. A later import of
the same module skips re-parsing and re-compiling, as long as the source file has not changed.

**Common mistakes in understanding this process:**
- thinking Python interprets source code line by line without an intermediate bytecode step;
- thinking `.pyc` is cached for scripts run directly as `__main__` – it is not;
- confusing the AST level (the language's structure) with the bytecode level (a CPython
  implementation detail).

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
