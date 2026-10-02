---
id: emb-dtypes-0014
title: "What is integer promotion in C?"
description: "Integer promotion converts integer types with rank no greater than int to int or unsigned int in expressions specified by the standard."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 4
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
---

## Short answer

Integer promotion is the **automatic conversion** of an integer type with rank no greater than `int` to `int` or `unsigned int` in expressions where the C standard requires it. If `int` can represent every value of the original type, the result is `int`; otherwise it is `unsigned int`.

For example, `uint8_t` usually promotes to `int`, while a 16-bit `unsigned int` may remain `unsigned int`; this depends on the implementation's ranges.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
