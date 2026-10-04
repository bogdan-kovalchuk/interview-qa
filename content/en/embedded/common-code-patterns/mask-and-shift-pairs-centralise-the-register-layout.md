---
id: emb-patterns-0033
title: "Why define register fields as MASK plus SHIFT rather than magic numbers?"
description: "MASK+SHIFT pairs are self-documenting and centralize the register layout"
track: embedded
section: common-code-patterns
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

**MASK+SHIFT pairs are self-documenting and centralize the register layout.**

`(reg & PRESC_MASK) >> PRESC_SHIFT` clearly states which field is being read; magic `(reg & 0x70) >> 4` scattered across code is easy to desynchronize from the datasheet.

Rule: one `#define` MASK and one SHIFT per field; use them for both reading and read-modify-write.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
