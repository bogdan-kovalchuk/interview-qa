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
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
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

The pointer address cannot be changed: `reg = other` violates a language constraint and requires a diagnostic. The data at that address has type `volatile uint32_t`, so accesses to it follow the volatile rules of the implementation. This is a typical type for a fixed address of a writable hardware register.[^iso-c-n1570]

Embedded use case: the address of a GPIO output register is constant, while the register contents can change by hardware or by firmware writes.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
