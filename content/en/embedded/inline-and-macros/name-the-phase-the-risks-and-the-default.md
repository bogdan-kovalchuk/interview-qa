---
id: emb-macros-0047
title: "What should a candidate say when asked to choose between a macro and `inline`?"
description: "Distinguish preprocessing from compilation, list macro risks such as double evaluation and precedence bugs, and default to static inline."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 4
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**Distinguish the phase, list the macro risks, and default to `static inline`.**

Strong answer: preprocessing is not compilation; a macro is text without types or scope, at risk of double evaluation and precedence bugs; `static inline` gives the same speed plus type safety, single evaluation, and debuggability. Macros I keep for register defs, conditional compilation, `#`/`##`, X-macros, `STATIC_ASSERT`, and I mention MISRA C (Motor Industry Software Reliability Association C) 4.9/20.7.

Rule: do not stop at syntax – explain why and when.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
