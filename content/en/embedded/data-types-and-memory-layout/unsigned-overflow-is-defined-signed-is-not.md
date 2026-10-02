---
id: emb-dtypes-0049
title: "What is unsigned integer overflow, and how does it differ from signed overflow?"
description: "Unsigned overflow is defined by the standard as modular arithmetic, while signed overflow is undefined behavior."
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

Arithmetic in an unsigned type is defined modulo `2^N`, where `N` is that type's width; signed overflow is instead <span class="warn">undefined behavior</span> in C. However, `uint8_t` and often `uint16_t` operands are promoted to `int` first, so the addition `255 + 1` can produce `256`, with zero appearing when the result is converted back to `uint8_t`.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
