---
id: emb-structs-0007
title: "What is `offsetof` and what is it needed for?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**`offsetof(T, field)`** returns the offset of a field inside a struct in bytes.

This standard macro from `<stddef.h>` can verify layout without manual counting. In embedded, it is used in static assertions for register maps, protocol headers, Flash records, and DMA descriptors.

If the hardware manual specifies `STATUS` at offset `0x10`, this can be checked with `_Static_assert(offsetof(Type, STATUS) == 0x10, "...")`. `offsetof` must not be used with bit-field members.[^iso-c-n1570]

## Detailed explanation

TODO
