---
id: emb-cppfound-0032
title: "What does this print?"
description: "Pointer subtraction yields ptrdifft, the number of elements between two pointers, not bytes."
track: embedded
section: c-in-embedded
level: junior
type: concept
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
int arr[]={1,2,3,4,5};
int *p=arr+4;
int *q=arr+1;
printf("%td", p-q);
```

## Short answer

`3`.

Pointer subtraction (`p - q`) returns `ptrdiff_t` – the number of **elements between them**, not bytes: `(arr+4) - (arr+1) = 3` elements.

`%td` – the format specifier for `ptrdiff_t`. The result can be negative if `q > p`.

Physically: the byte difference = `3 * sizeof(int) = 12` bytes, but pointer subtraction divides by `sizeof(int)`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
