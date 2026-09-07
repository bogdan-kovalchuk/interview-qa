---
id: emb-volconst-0012
title: "What does `volatile uint32_t * const reg` mean?"
description: "reg is a const pointer to volatile uint32t; the address is fixed but every dereference is a real volatile access."
track: embedded
section: volatile-and-const
level: junior
type: concept
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

## Short answer

**`reg` is a const pointer to volatile `uint32_t`**.

The pointer address cannot be changed: `reg = other` is a compile error. But the data at that address is volatile: every `*reg` is read or written for real. This is the canonical type for a fixed writable hardware register.

Embedded use case: the address of a GPIO output register is constant, while the register contents can change by hardware or by firmware writes.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
