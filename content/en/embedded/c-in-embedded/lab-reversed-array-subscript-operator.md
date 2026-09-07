---
id: emb-cppfound-0078
title: "What does this code print?"
description: "Why the reversed subscript expression is valid C pointer arithmetic."
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
int arr[]={5,10,15};
printf("%d", 2[arr]);
```

## Short answer

`15`. `2[arr]` -> per the standard: `*(2 + arr)` – identical to `arr[2]`. The subscript operator is symmetric due to addition commutativity: `arr[2] == *(arr+2) == *(2+arr) == 2[arr]`. All four forms produce the same code; `2[arr]` is valid C but unreadable, often seen as an interview question to test understanding of pointer arithmetic.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
