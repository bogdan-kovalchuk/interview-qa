---
id: emb-cppfound-0006
title: "Trap: why does sizeof(arr) in a function return 4 or 8 instead of the array size?"
description: "An array parameter decays to a pointer inside a function, so sizeof returns the pointer size rather than the array size; pass the length explicitly to avoid silent truncation."
track: embedded
section: c-in-embedded
level: junior
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
    applicability: "Origin of the question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

When an array is passed to a function, it <span class="warn">decays to a pointer</span>: `void f(int arr[])` ≡ `void f(int *arr)`.

`sizeof(arr)` inside the function = `sizeof(int*)` = 4 or 8 (pointer size), not the array size.

Real case: changed `int16_t buffer[256]` to `int16_t *buffer` but kept `sizeof(buffer)/sizeof(buffer[0])` -> processed only 2 elements instead of 256.

Solution: pass the size explicitly: `void f(int *arr, size_t n)`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
