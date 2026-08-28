---
id: py-fund-0007
title: "What risks arise if code relies on CPython-specific behaviour when porting to PyPy or another Python implementation?"
description: "What risks arise if code relies on CPython-specific behaviour when porting to PyPy or another Python implementation?"
track: python
section: fundamentals
level: senior
type: practical
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L27-L46
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Such code can lose correctness, portability or the expected performance characteristics.**[^py314-reference-executionmodel] Another implementation may have a different garbage collector, a different moment of finalization, different bytecode, a JIT and a different object layout. Rely on documented language semantics, manage resources through context managers, and test on the target implementations.

## Detailed explanation

The Python language and its implementation are different things. The Language Reference describes
the semantics every implementation must honour; everything else - how exactly CPython achieves it -
may differ in PyPy, GraalPy or MicroPython.[^py314-reference-executionmodel]

The most common implicit dependency is the moment an object is destroyed. CPython uses reference
counting, so an object disappears as soon as the last reference is gone, and a file opened without
`with` closes "by itself". In PyPy the collector is different, the moment of finalization is
undefined, and the same code holds the file descriptor until the next collection.

```python
data = open('report.csv').read()   # CPython: the file closes right away
                                   # PyPy: the descriptor stays open, unpredictably long

with open('report.csv') as f:      # both: closed at the end of the block, by contract
    data = f.read()
```

The second dependency is the identity of small objects. CPython caches small integers and some
strings, so `a is b` is often true for equal small values. That is an implementation cache, not a
rule of the language: values are compared with `==`, while `is` checks
identity.[^py314-reference-datamodel]

The third is bytecode and `dis`. The code object format, the opcode set and the output of `dis` are
documented as a CPython detail and change between versions, so any code parsing disassembled output
breaks on the next release.[^py314-faq-general]

**The categories of risk worth naming separately:**
- **correctness**: relying on immediate finalization or on destruction order leaks resources on
  another implementation;
- **portability**: a C extension built against the CPython ABI simply will not load where the ABI
  differs;
- **performance**: the assumption "string concatenation in a loop is cheap" rests on a CPython
  optimisation another implementation may lack - and conversely, a JIT makes fast what is slow in
  CPython;
- **compatibility over time**: an implementation detail can change between 3.13 and 3.14 without any
  warning, precisely because no guarantee was given for it.

The practical rule is simple: if a behaviour is not in the Language Reference, or is marked as an
implementation detail, it must not become part of your code's contract. Resources are closed through
context managers, equality is checked with `==`, and assumptions about speed are checked by
measuring on the implementation the code will actually run on.

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
