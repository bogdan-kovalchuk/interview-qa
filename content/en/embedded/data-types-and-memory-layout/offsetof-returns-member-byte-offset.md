---
id: emb-dtypes-0054
title: "What is `offsetof()` for, and where is it defined?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`offsetof(type, member)` from `<stddef.h>` returns the byte offset of an ordinary structure member from the start; it cannot be applied to a bit-field.[^iso-c-n1570]

Usage:
1. Layout check: `static_assert(offsetof(CanFrame, crc) == 6, "Wrong layout");` (if that is genuinely required by a particular ABI/protocol).
2. Serialization/deserialization;
3. **container_of** macro (Linux kernel) - obtain a struct* from a member*.

The value depends on the implementation's layout; the macro itself does not define a protocol layout.[^iso-c-n1570]

## Detailed explanation

TODO
