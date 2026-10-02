---
id: emb-dtypes-0077
title: "What is the promotion rule, and how does C handle expressions with `char` and `short`?"
description: "Before arithmetic, char and short automatically promote to int, which can surprise bitwise operations."
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
---

## Short answer

**Integer promotion** converts narrow integer operands before operations for which the standard requires promotions: a value becomes `int` if it can represent every value of the original type, and otherwise `unsigned int`.[^iso-c-n1570] Thus `uint8_t`, when that optional typedef is available, commonly promotes to `int`, but the result of bitwise `~` has type `int`, not `uint8_t`. Converting the result back to `uint8_t` narrows it; do not rely on a particular representation of negative `int` in a portable example.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
