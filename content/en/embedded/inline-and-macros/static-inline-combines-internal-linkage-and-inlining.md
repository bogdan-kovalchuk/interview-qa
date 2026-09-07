---
id: emb-macros-0008
title: "Why is `static inline` considered the modern replacement for function-like macros?"
description: "Static inline combines internal linkage with inline expansion and avoids external symbol conflicts between translation units."
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

**`static inline`** combines internal linkage with the ability to be expanded inline.

It goes in a header, provides type safety and single evaluation of arguments, does not create an extra external symbol and does not conflict between translation units (TU): each TU gets its own internal definition or fully inlined code. The compiler chooses between expansion and a call based on optimization.

Embedded rule: bit manipulations, small helpers and computations with arguments belong in `static inline` in a header, not in a macro.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
