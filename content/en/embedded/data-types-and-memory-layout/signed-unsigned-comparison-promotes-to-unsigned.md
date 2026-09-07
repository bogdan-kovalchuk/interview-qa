---
id: emb-dtypes-0003
title: "Why does `if(x < y)` return `false` when `int x = -1` and `unsigned int y = 1`?"
description: "In a mixed expression the signed value converts to unsigned, so -1 becomes UINTMAX."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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

<span class="warn">Integer promotion rule</span>: when mixing signed and unsigned in one expression, the signed value converts to unsigned.

`-1` (int) -> `UINT_MAX` (4,294,967,295) when converted to `unsigned int`. Therefore `UINT_MAX < 1` -> `false`.

Protection: enable `-Wsign-compare`, compare identical types.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
