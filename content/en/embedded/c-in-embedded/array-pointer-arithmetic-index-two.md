---
id: emb-cppfound-0008
title: "What does this print?"
description: "Pointer arithmetic with p+2 reaches arr[2] and dereferences to 30; the standard defines arr[i], (arr+i), (i+arr) and i[arr] as equivalent."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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
int arr[5] = {10,20,30,40,50};
int *p = arr;
printf("%d", *(p+2));
```

## Short answer

`30`.

`arr` decays to a pointer to the first element. `p = arr` -> `p` points to `arr[0]`.

`p+2` -> pointer to `arr[2]` (step of `2 * sizeof(int) = 8` bytes on 32-bit). `*(p+2)` -> dereference -> `arr[2] = 30`.

Per the standard: `arr[i] ≡ *(arr+i) ≡ *(i+arr) ≡ i[arr]` – all four forms are equivalent.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
