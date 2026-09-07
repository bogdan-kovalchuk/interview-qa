---
id: emb-cppfound-0005
title: "What does this print?"
description: "Pointer arithmetic scales by sizeof the pointed-to type, so a uint8t pointer increments by one byte and a uint32t pointer by four bytes."
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
uint8_t *p = (uint8_t*)0x1000;
p++;
printf("%p", (void*)p);
```

## Short answer

`0x1001`.

Pointer arithmetic scales by `sizeof(*p)`. For `uint8_t*`: `sizeof(uint8_t) = 1`, so `p++` -> address + 1 byte.

If `uint32_t *p = (uint32_t*)0x1000; p++;` -> `0x1004` (step of 4 bytes).

Rule: `p + n` = `(char*)p + n * sizeof(*p)`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
