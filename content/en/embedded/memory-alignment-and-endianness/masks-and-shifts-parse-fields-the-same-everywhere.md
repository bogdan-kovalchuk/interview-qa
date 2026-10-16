---
id: emb-align-0036
title: "Why are masks and shifts on a `uint32_t` more portable than unions or bitfields for parsing fields?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Shifts and masks on the same unsigned value extract the same logical bits.**

For `uint32_t reg`, `(reg >> 4) & 0x7` extracts bits 4–6 of the numeric value itself; the result does not depend on how its bytes are laid out in memory.

First decode bytes according to the format, then use shifts and masks; C leaves bitfield allocation and packing to the implementation.[^iso-c-n1570]

## Detailed explanation

TODO
