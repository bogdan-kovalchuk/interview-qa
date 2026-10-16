---
id: emb-structs-0053
title: "Trap: can you rely on C struct layout across different compilers without checking?"
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

<span class="warn">No: ABI, alignment, packing pragmas, and bit-field rules can differ.</span>

Even identical source can have different offsets or size on another architecture. For a host tool plus MCU firmware this is a frequent bug: the PC tool writes a binary file per its struct layout, the firmware reads it per a different one.

Mitigation: describe external binary formats in bytes, not in C structs. Add version, length, endian, and static/runtime checks.[^iso-c-n1570]

## Detailed explanation

TODO
