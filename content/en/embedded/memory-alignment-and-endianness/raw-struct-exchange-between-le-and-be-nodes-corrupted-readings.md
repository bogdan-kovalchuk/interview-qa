---
id: emb-align-0024
title: "Pitfall: why can exchanging raw C structs between LE and BE nodes corrupt data?"
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

<span class="warn">Exchanging raw C structs between LE and BE nodes does not define a portable data format.</span>

The byte order of numeric fields, padding, alignment, and even type sizes can depend on the implementation. The field offset and bytes on the wire cannot be inferred from the names M4 and PowerPC alone.

Guard: define a wire format and serialize each field explicitly; specify its width and byte order.[^iso-c-n1570]

## Detailed explanation

TODO
