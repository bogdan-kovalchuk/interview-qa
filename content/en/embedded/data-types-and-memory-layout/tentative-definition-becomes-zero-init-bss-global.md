---
id: emb-dtypes-0094
title: "What is a tentative definition in C, and where does it end up?"
description: "In C, a file-scope tentative definition becomes a zero-initialized definition if the translation unit has no other definition."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
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
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
  - source_id: gcc-codegen-options
    title: "GCC: Options for Code Generation Conventions"
    url: https://gcc.gnu.org/onlinedocs/gcc/Code-Gen-Options.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Documents the GCC -fcommon and -fno-common behavior for global tentative definitions; behavior is GCC-specific."
  - source_id: cpp-basic-def
    title: "C++ draft: Declarations and definitions"
    url: https://eel.is/c++draft/basic.def
    accessed: 2026-10-04
    kind: spec
    version: "current working draft"
    applicability: "Supports the declaration/definition distinction in C++; it does not describe C language rules."
---

## Short answer

**Tentative definition** is a file-scope object declaration without an initializer or `extern`, such as `int x;`. If no ordinary definition of the same identifier appears in that translation unit, C treats it as a definition with zero initialization; the standard does not require placement in `.bss`.[^iso-c-n1570]

In GCC, placement in a common block depends on `-fcommon`; with `-fno-common`, same-name definitions from multiple files can fail at link time. C++ has no tentative-definition concept.[^gcc-codegen-options] [^cpp-basic-def]
## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
