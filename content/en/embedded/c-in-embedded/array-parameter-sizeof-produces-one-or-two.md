---
id: emb-cppfound-0016
title: "Trap: what value does sizeof(arr)/sizeof(arr[0]) produce in this function?"
description: "In a function parameter int arr[] decays to int, so sizeof(arr)/sizeof(arr[0]) yields 1 or 2, not the array length."
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

`n = 1` (on 32-bit) or `n = 2` (on 64-bit).

In a function parameter, `int arr[]` ≡ `int *arr` – decay to a pointer. `sizeof(arr) = sizeof(int*) = 4` (or 8). `sizeof(arr[0]) = sizeof(int) = 4`. So `4/4 = 1`;

<span class="warn">Not 8, not 256, not the array size</span> – only 1 or 2;

Always pass the size explicitly: `void f(int *arr, size_t n)`; safeguard: `_Static_assert` at the caller.[^embeddedinterviewlab]

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
