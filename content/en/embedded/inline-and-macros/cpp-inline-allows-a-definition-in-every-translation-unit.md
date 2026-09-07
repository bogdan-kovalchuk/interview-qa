---
id: emb-macros-0048
title: "How does the meaning of `inline` differ between C and C++?"
description: "In C++ inline allows duplicate definitions across translation units via the linker, while in C99 plain inline needs an extern declaration in one TU."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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

In C++, an `inline` function may be defined in multiple translation units (TUs) through a header without violating the ODR (One Definition Rule) – the linker merges the copies; this is the standard way to put functions in a header.

In C (C99+) the rules are more complex: plain `inline` provides only an inline definition with no external symbol, so an `extern` declaration is needed in one TU, or more simply, `static inline`.

Rule: in C, for header functions almost always write `static inline`; in C++, plain `inline` is enough.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
