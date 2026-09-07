---
id: emb-macros-0019
title: "What does MISRA C Rule 4.9 require about function-like macros?"
description: "MISRA C requires preferring functions over function-like macros where they are interchangeable."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**MISRA C (Motor Industry Software Reliability Association C) requires preferring functions over function-like macros** where they are interchangeable.

Rationale: macros bypass type checking, can evaluate arguments unpredictably (double evaluation) and complicate debugging and static analysis.

Practical consequence: in safety-critical projects, replace function-like macros with `static inline`; keep macros only for what cannot be a function (register defs, conditional compilation, X-macros).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
