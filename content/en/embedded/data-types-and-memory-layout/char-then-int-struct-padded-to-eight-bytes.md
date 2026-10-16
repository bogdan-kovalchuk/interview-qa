---
id: emb-dtypes-0010
title: "Under AAPCS32, what size does `struct { char c; int x; }` have?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: aapcs32-layout
    title: "Procedure Call Standard for the Arm Architecture (AAPCS32)"
    url: https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst
---

## Short answer

Under AAPCS32, `struct { char c; int x; }` is expected to occupy 8 bytes: `c` has offset 0, `x` offset 4, and there are 0 bytes of trailing padding. This follows from a 1-byte `char`, a 4-byte `int` aligned to 4 bytes, and struct alignment matching its strictest member; this is a target ABI result, not a general C language guarantee. Check the actual layout with `sizeof` and `offsetof`.[^aapcs32-layout]

## Detailed explanation

TODO
