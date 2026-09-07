---
id: emb-structs-0009
title: "Trap: what is wrong with this register map?"
description: "Reserved gaps between registers may be missing."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
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
typedef struct {
    volatile uint32_t CR;
    volatile uint32_t SR;
    volatile uint32_t DR;
} UART_TypeDef;
```

## Short answer

<span class="warn">Reserved gaps between registers may be missing.</span>

A hardware register map often has address gaps. If the manual says `DR` is at offset `0x10` but the struct places it at offset `0x08`, all accesses after the gap will be wrong. `volatile` does not fix an incorrect layout.

Defense: add reserved fields of the correct size, for example `uint32_t RESERVED0[2]`, and verify with `offsetof`.[^embeddedinterviewlab]

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
