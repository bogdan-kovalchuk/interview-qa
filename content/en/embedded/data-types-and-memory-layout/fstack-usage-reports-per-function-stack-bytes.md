---
id: emb-dtypes-0058
title: "How do you check a function's stack frame size in GCC?"
description: "The -fstack-usage flag makes GCC emit .su files reporting each function's stack frame size."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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
  - source_id: gcc-stack-usage
    title: "GCC: Developer Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/Developer-Options.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Describes .su format, qualifier meanings, and limits of GCC -fstack-usage reports; it does not define the program's total stack budget."
---

## Short answer

The `-fstack-usage` option makes GCC emit a `.su` report estimating stack usage per function.[^gcc-stack-usage]

Each `.su` entry has four tab-separated fields: source location and function name, mangled name, byte count, and qualifiers such as `static`, `dynamic`, or `bounded`.[^gcc-stack-usage]

The report describes an individual function, not the total maximum for a call path or task stack.[^gcc-stack-usage]

GCC also provides `-Wstack-usage=N` threshold warnings, but that threshold does not prove the full call path fits the available stack.[^gcc-stack-usage]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
