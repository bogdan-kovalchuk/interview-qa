---
id: emb-macros-0045
title: "Why are compiler errors inside a macro hard to read?"
description: "Macro diagnostics may point to the call site, definition, and nested expansion steps."
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
  - source_id: gcc-preprocessor-options
    title: "GCC: Preprocessor Options"
    url: https://gcc.sourceware.org/onlinedocs/gcc/Preprocessor-Options.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Documents GCC -E mode and tracking token locations across macro expansions; diagnostics formats can differ in other compilers."
---

## Short answer

**The error points to the expanded code, not to the `#define` line.**

The compiler analyzes tokens after preprocessor substitution, and modern compilers often show the expansion chain with both the call site and definition. Nested macros add more levels to that chain, making the error harder to read.

With GCC, `gcc -E` prints the preprocessed output, and `-ftrack-macro-expansion` controls tracking token locations in diagnostics. For nontrivial logic, choose a typed `static inline` function, which is easier to debug as ordinary code.[^gcc-preprocessor-options]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
