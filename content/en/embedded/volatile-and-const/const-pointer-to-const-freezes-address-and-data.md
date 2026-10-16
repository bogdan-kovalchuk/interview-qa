---
id: emb-volconst-0018
title: "What does `const uint8_t * const buf` mean?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**`buf` is a const pointer to const `uint8_t`**.

Neither the pointer address nor the data through the pointer can be changed. This is useful for a local alias to a read-only table, calibration data, or a read-only memory region.

Rule: the first `const` next to the base type guards the data; `const` after `*` guards the pointer itself.[^iso-c-n1570]

## Detailed explanation

TODO
