---
id: emb-cppfound-0018
title: "What does this print?"
description: "Why sizeof a dereferenced pointer depends on its pointer type."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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
uint32_t *p=(uint32_t*)0x2000;
uint8_t *q=(uint8_t*)p;
printf("%zu %zu", sizeof(*p), sizeof(*q));
```

## Short answer

`sizeof(*p)` -> **4**. Dereferencing `uint32_t*` yields an object of type `uint32_t` – 4 bytes.

`sizeof(*q)` -> **1**. Dereferencing `uint8_t*` yields `uint8_t` – 1 byte.

Key point: `sizeof` on a dereferenced operand is determined by the pointer type, not the address – both pointers point to the same address `0x2000`, but sizeof returns different values.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
