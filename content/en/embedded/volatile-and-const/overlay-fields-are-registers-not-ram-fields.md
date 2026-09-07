---
id: emb-volconst-0045
title: "Why are peripheral register struct fields declared `volatile`?"
description: "Each field of the struct overlay represents a hardware register, not an ordinary RAM field."
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

**Because each field of the struct overlay represents a hardware register, not an ordinary RAM field.**

When code writes `GPIOA->ODR` or reads `GPIOA->IDR`, this is a bus transaction to a peripheral address. The compiler must not cache a field value, merge writes, or remove reads.

Rule: in a CMSIS-style register overlay, volatile must be placed on the register fields or on the access type so that every field access is a volatile access.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
