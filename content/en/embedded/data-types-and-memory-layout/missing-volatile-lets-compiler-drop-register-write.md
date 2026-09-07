---
id: emb-dtypes-0098
title: "What happens with `uint32_t *ptr = (uint32_t*)0x40020000; *ptr = 0xFF;` without `volatile`?"
description: "Without volatile, the compiler may eliminate the write as a dead store, since nothing reads the pointer again."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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

The compiler may <span class="warn">eliminate the write as a dead store</span> (dead store elimination): `*ptr` is never read later in the program flow, so the compiler considers the write redundant.

Without `volatile`, there is <span class="warn">no guarantee</span> that the bytes actually reach the GPIO.

Correct approach: `volatile uint32_t * const GPIOA_ODR = (volatile uint32_t*)0x40020014U;` – every write/read is actually performed.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
