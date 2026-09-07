---
id: emb-macros-0037
title: "How do you define access to a memory-mapped register with a macro?"
description: "The macro expands into lvalue access to a fixed address for read and write of a memory-mapped register."
track: embedded
section: inline-and-macros
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
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
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Question code

```c
#define GPIOA_ODR \
  (*(volatile uint32_t *)0x40020014U)
```

## Short answer

**The macro expands into lvalue access to a fixed address**, so you can write `GPIOA_ODR = 0xFF;` and `x = GPIOA_ODR;`.

`volatile` prevents the compiler from caching or eliminating the access; the cast converts a numeric address to a typed pointer; the outer `*` dereferences it. The `U` suffix makes the literal unsigned.

Rule: this is one of the cases where a macro is justified – such an address constant is not conveniently expressed as a function.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
