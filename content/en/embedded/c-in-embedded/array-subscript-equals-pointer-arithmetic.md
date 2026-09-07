---
id: emb-cppfound-0093
title: "What is printed?"
description: "Why array subscripting and pointer arithmetic are equivalent in C."
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
int arr[4]={10,20,30,40};
printf("%d %d",*(arr+3), arr[3]);
```

## Short answer

Both print `40`.

`*(arr+3)` -> pointer arithmetic: offset by 3 elements, dereference = `arr[3] = 40`. `arr[3]` -> subscript operator, by definition = `*(arr+3)`.

They are **identical per the standard**. The compiler generates the same machine code for both variants.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
