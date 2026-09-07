---
id: emb-cppfound-0013
title: "What does this example print?"
description: "Array subscript arr[2] is defined as (arr+2), so even 2[arr] works via commutativity of addition."
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
int arr[3] = {1,2,3};
printf("%d %d", arr[2], *(arr+2));
```

## Short answer

Both expressions print **3** and are fully equivalent per the C standard.

`arr[2]` -> the standard defines it as `*(arr+2)`: `2 * sizeof(int) = 8` bytes are added to the address `arr`, then dereferenced.

Therefore even `2[arr]` -> `*(2+arr)` -> 3 – also valid (due to commutativity of addition, although unreadable).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
