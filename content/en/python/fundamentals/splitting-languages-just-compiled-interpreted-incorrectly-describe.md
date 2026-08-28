---
id: py-fund-0002
title: "Why does splitting languages into just \"compiled\" and \"interpreted\" incorrectly describe Python?"
description: "Why does splitting languages into just \"compiled\" and \"interpreted\" incorrectly describe Python?"
track: python
section: fundamentals
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
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

**Compilation and interpretation describe different stages of execution, so they are not mutually exclusive labels for a language.**[^py314-reference-executionmodel] CPython, for example, compiles source code into bytecode, after which the interpreter executes that bytecode. Another Python implementation may apply a JIT or a different internal representation without changing the core semantics of the language.

## Detailed explanation

Compilation and interpretation are properties of an **implementation**, not of a language.
Compilation means translating code from one form into another before execution; interpretation means
executing code in some representation. A language defines only semantics, not the way somebody
carries them out.

The question "is Python compiled or interpreted?" is therefore posed wrongly. The right question is
about a specific implementation. CPython does **both**: it compiles source into bytecode, and then
interprets that bytecode in the virtual machine loop.[^py314-reference-executionmodel]

```python
# CPython does both steps, in this order:
source.py  ->  parse  ->  AST  ->  compile  ->  code object (bytecode)
                                                     |
                                                     v
                                        the VM interprets the bytecode
```

Other implementations arrange the same stages differently. PyPy interprets bytecode and compiles hot
regions to machine code at run time (a JIT). Cython translates a subset of Python into C, which is
then built by an ordinary compiler. None of them changes the semantics of the language - only the
route to execution changes.

The same confusion exists for other languages. Java compiles to bytecode executed by the JVM, often
with a JIT. JavaScript in modern engines is compiled to machine code, though historically it was
called interpreted. C is usually compiled, yet C interpreters exist.

**What is actually worth distinguishing instead of the labels:**
- **into what** the code is translated: bytecode, machine code, or another language;
- **when** that happens: ahead of time, on first run, or on the hot path (JIT);
- **what executes the result**: the processor directly, or a virtual machine;
- **what the language guarantees of this**: in Python's case, none of the above - they are all
  implementation details.[^py314-faq-general]

The practical consequence: the claim "Python is slow because it is interpreted" is incorrect by
construction. Speed is decided by the specific implementation and the workload, not by a label; the
same code on PyPy can be several times faster with no change to the
source.[^py314-reference-datamodel]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
