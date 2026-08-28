---
id: py-fund-0001
title: "What stages does a Python module go through from source code to executing runtime instructions, and at which stage can bytecode appear?"
description: "What stages does a Python module go through from source code to executing runtime instructions, and at which stage can bytecode appear?"
track: python
section: fundamentals
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L38-L67
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**In CPython the source is first compiled into a code object holding bytecode, and that code object is then executed by the interpreter.**[^py314-reference-executionmodel] Before the code object exists the code goes through parsing and the construction of an AST, so bytecode appears at compile time, ahead of execution. During import, usable bytecode may additionally be cached in a `.pyc` file.

## Detailed explanation

The route from program text to execution in CPython has two large phases: compilation and execution.
Compilation turns text into a code object; execution is the virtual machine's work on the bytecode
inside that code object.[^py314-reference-executionmodel]

Compilation in turn divides into steps. Tokenization first splits the text into lexemes, the parser
then builds an abstract syntax tree from them, and only then does the compiler walk that tree and
emit bytecode together with the tables of constants and names. That is why a syntax error surfaces
before a single line has run.

```python
source text  ->  tokens  ->  AST  ->  code object (bytecode + constants + names)
                                            |
                                            v
                                   the VM executes it frame by frame
```

The result of compilation - the code object - is reachable from inside the language too: `compile()`
produces one explicitly, and `dis.dis()` shows the bytecode in readable form. That is useful for
understanding, but the format itself is a CPython implementation detail.[^py314-faq-general]

Execution begins with the interpreter creating a frame - a context with a local namespace, a
reference to globals and a position in the bytecode - and running the instructions one after
another. Every function call creates a new frame; returning destroys it.

**Where import and `.pyc` enter this chain:**
- on importing a module, CPython first looks for a ready code object in `__pycache__`;
- if the cache is absent or stale, the module is compiled anew and the cache is rewritten;
- the code object is then **executed**: the module body runs top to bottom, creating functions,
  classes and other names in the module namespace;
- importing the same module again repeats none of this - the module comes from
  `sys.modules`.[^py314-reference-datamodel]

The main thing to take away: bytecode appears at compile time, before execution, not "on the fly
while running". And a `.pyc` is only a cache of the first phase, changing neither the second phase
nor the semantics.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
