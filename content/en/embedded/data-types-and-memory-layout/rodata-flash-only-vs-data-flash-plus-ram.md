---
id: emb-dtypes-0072
title: "What is the resource difference between `.rodata` in Flash and `.data` in RAM?"
description: ".rodata is read straight from Flash at no RAM cost, while .data pays for both Flash and RAM."
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

**.rodata** – Flash only: the CPU reads constants directly from there (with wait states), no RAM is spent.

**.data** – both Flash and RAM: values in Flash (LMA) + a copy in RAM (VMA). That is, <span class="warn">double cost</span>: Flash for initialization values + RAM for runtime.

Practice on an MCU with 20KB RAM: a large lookup table -> `const` -> `.rodata` -> Flash only. Saving RAM is critical.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
