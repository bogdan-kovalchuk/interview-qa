---
id: emb-align-0041
title: "Trap: why can the same `struct` in source have a different binary layout?"
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

<span class="warn">Padding and alignment depend on the compiler, architecture, and build options.</span>

The same code on M4 and PowerPC may have different field offsets, while endianness determines the byte order of multi-byte values. So "the same .h file" ≠ "the same byte format".

Defense: do not assume two compilers have compatible layouts without checking; define an explicit wire format and serialize field by field.[^iso-c-n1570]

## Detailed explanation

TODO
