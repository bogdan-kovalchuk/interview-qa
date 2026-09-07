---
id: emb-structs-0046
title: "Why are `volatile` on a struct pointer and `volatile` on its fields not always the same?"
description: "The volatile qualifier must apply at the type level through which the access occurs."
track: embedded
section: structs-unions-and-bitfields
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

**The qualifier must apply at the type level through which the access occurs.**

`volatile GPIO_TypeDef *GPIOA` makes accesses to members volatile-qualified through that pointer. But if a non-volatile alias to the same object is obtained somewhere, accesses through it will not have volatile semantics. In CMSIS, volatile is typically placed in typedef fields or access macros.

Rule: the register access API must not allow accidentally bypassing the volatile-qualified path.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
