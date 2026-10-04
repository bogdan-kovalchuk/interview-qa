---
id: emb-macros-0025
title: "When do you choose `static inline` and when a function-like macro?"
description: "static inline is for everything function-like: small helpers, type-safe bit manipulation, and single-evaluation argument computations."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
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

**`static inline`** is for everything that resembles a function: small helpers, type-safe bit manipulation, computations with arguments (exactly one evaluation of each).

A macro is only for what cannot be a function: working with tokens/names (`#`, `##`), conditional compilation, register address definitions, X-macros, `STATIC_ASSERT`.

Rule: default to `static inline`; a macro is an exception that requires justification.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
