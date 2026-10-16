---
id: emb-dtypes-0099
title: "Why use `static_assert` when working with structs in embedded systems?"
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

`static_assert` (C11 `_Static_assert`, C++ `static_assert`) checks a constant expression at compile time and diagnoses a false condition.[^iso-c-n1570]

For embedded: `static_assert(sizeof(CanFrame) == 13, "Wrong CAN frame size");`
`static_assert(offsetof(UartPacket, crc) == 6, "CRC offset mismatch");`

These checks pin expected size and offsets for a particular build; they do not guarantee the same layout under other ABIs or full protocol conformance.

For a binary format, check the required `sizeof` and `offsetof`, and define portable field encoding separately.[^iso-c-n1570]

## Detailed explanation

TODO
