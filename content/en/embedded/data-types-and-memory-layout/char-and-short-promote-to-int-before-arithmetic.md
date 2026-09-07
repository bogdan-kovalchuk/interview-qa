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
updated: 2026-09-07
content_revision: 2
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
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Integer promotion** (C §6.3.1.1): before most arithmetic operations, `char`, `signed char`, `unsigned char`, `short`, `unsigned short` are automatically promoted to `int` (or `unsigned int`).

Unexpected result: `uint8_t a = 200; uint8_t b = ~a;` – `a` -> `int(200)`, NOT -> `int(0xFFFFFF37 = -201)`, truncated to `uint8_t: 55`.

Always understand promotion before the operation.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
