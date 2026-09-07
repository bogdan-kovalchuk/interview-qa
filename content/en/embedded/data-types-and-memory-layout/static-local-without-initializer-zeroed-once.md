---
id: emb-dtypes-0041
title: "Trap: is this zero-initialized inside a function? `static int x;`"
description: "A static local without an initializer is equivalent to static int x = 0 and is zeroed only once, at boot."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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

**Yes**, but there is a subtlety: a `static` local without an initializer ≡ `static int x = 0;` – zero on the first call (zeroed in `.bss` at boot).

`static int x = 5;` -> initialized to 5 once. Subsequent changes persist between calls.

A <span class="warn">regular</span> `int x;` is NOT initialized (garbage). The mistake is assuming `int x;` = 0 on the first call.[^embeddedinterviewlab]

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
