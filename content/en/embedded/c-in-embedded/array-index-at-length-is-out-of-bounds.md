---
id: emb-cppfound-0030
title: "Trap: what is wrong?"
description: "Index 5 on a 5-element array is out of bounds, causing undefined behavior that may silently corrupt data or crash on return."
track: embedded
section: c-in-embedded
level: junior
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Question code

```c
int arr[5];
arr[5] = 0;
```

## Short answer

<span class="warn">Out-of-bounds write -> undefined behavior.</span> Valid indices: `0..4`. `arr[5]` – beyond the array.

In memory `arr[5]` sits right after the array: it may be another local variable, a return address, a saved LR.

Consequences: silent data corruption or a crash on function return (corrupted return address);

Protection: `-fsanitize=address`, explicit index checks, `static_assert(i < ARRAY_SIZE)`.[^embeddedinterviewlab]

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
