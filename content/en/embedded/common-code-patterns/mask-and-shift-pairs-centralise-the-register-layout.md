---
id: emb-patterns-0033
title: "Why define register fields as MASK plus SHIFT rather than magic numbers?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**MASK+SHIFT pairs are self-documenting and centralize the register layout.**

`(reg & PRESC_MASK) >> PRESC_SHIFT` clearly states which field is being read; magic `(reg & 0x70) >> 4` scattered across code is easy to desynchronize from the datasheet.

Rule: one `#define` MASK and one SHIFT per field; use them for both reading and read-modify-write.[^iso-c-n1570]

## Detailed explanation

TODO
