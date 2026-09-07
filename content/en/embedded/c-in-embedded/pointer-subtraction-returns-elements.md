---
id: emb-cppfound-0091
title: "Trap: what is printed?"
description: "Why subtracting pointers returns an element distance rather than a byte count."
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
    applicability: "Origin of the question and answer; answer not independently verified."
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
int *p=arr+3;
int *q=arr+1;
printf("%td", p-q);
```

## Short answer

`2`. This is not a trap, but it tests understanding of pointer subtraction.

The real trap: people expect a <span class="warn">byte difference</span> (8 bytes) but get the **element count** (2). `p - q` = `(arr+3) - (arr+1) = 2`.

Byte difference: `2 * sizeof(int) = 8`. But `ptrdiff_t` returns elements; for a byte difference: `(char*)p - (char*)q` or `(uintptr_t)p - (uintptr_t)q`.[^embeddedinterviewlab]

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
