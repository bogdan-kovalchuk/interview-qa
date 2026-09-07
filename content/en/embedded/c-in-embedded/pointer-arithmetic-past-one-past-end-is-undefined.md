---
id: emb-cppfound-0040
title: "Trap: UB?"
description: "Why pointer arithmetic beyond one-past-the-end is undefined behavior."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 4
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
int arr[4]={0};
int *p=arr;
p+=5;
*p=1;
```

## Short answer

<span class="warn">Yes, undefined behavior</span> (even without dereferencing).

Forming the pointer `p += 5` goes beyond the array by more than one: `arr` has 4 elements, so valid pointers are `arr` through `arr+4` (inclusive of "one-past-the-end"). `arr+5` -> undefined behavior already at formation.

One-past-the-end (`arr+4`) – may be formed, but <span class="warn">must not be dereferenced</span>.[^embeddedinterviewlab]

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
