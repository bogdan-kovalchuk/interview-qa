---
id: emb-macros-0023
title: "What are macros still irreplaceable for, even in a MISRA project?"
description: "Macros remain essential for register addresses, compile-time utilities, conditional compilation, X-macros, and token operations."
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

Where `static inline` cannot replace the preprocessor:

• Register addresses with `volatile` cast; • utilities that cannot be functions: `ARRAY_SIZE`, `UNUSED`, `STATIC_ASSERT`; • Conditional compilation (`#ifdef`, `#if defined`); • X-macros and code generation; • stringification (`#`) and token pasting (`##`).

Rule: a macro is for textual/compile-time tricks; `static inline` is for everything that behaves like a function.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
