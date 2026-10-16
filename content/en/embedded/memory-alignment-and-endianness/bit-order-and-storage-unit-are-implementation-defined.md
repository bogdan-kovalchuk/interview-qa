---
id: emb-align-0034
title: "Trap: why is bitfield layout not portable between platforms?"
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

<span class="warn">C leaves bitfield allocation order within a storage unit and some packing rules to the implementation.</span>

Different ABIs and compilers can lay out fields differently, so the same struct does not define a portable byte representation for a protocol.

For protocols and registers, define the wire format explicitly and parse the integer value with masks and shifts.[^iso-c-n1570]

## Detailed explanation

TODO
