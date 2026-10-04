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
  - source_id: cppreference-inline
    title: "cppreference: inline specifier"
    url: https://en.cppreference.com/w/cpp/language/inline
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "C++ inline specifier: an inline function with external linkage may have one definition in each translation unit, provided the definitions agree."
---

## Short answer

In C++, an `inline` function may be defined in multiple translation units (TUs) through a header when the definitions meet ODR (One Definition Rule) requirements; this is a standard way to define functions in a header.[^cppreference-inline][^embeddedinterviewlab]

In C (C99+) the rules are more complex: plain `inline` provides only an inline definition with no external symbol, so an `extern` declaration is needed in one TU, or more simply, `static inline`.

In C, `static inline` is often used for header functions; in C++, `inline` permits multiple definitions under ODR conditions.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
