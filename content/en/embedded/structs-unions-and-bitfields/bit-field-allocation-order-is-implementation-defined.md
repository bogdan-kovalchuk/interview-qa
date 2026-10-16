---
id: emb-structs-0028
title: "Trap: is bit-field allocation order in memory portable?"
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

<span class="warn">No: the allocation order of bit-fields within a storage unit is implementation-defined.</span>

One compiler may place the first field in the least significant bits; another compiler or a different ABI may behave differently. Endianness also does not give a simple portable rule for bit-field layout within bytes.

Defence: do not use bit-fields as a wire format between different compilers/targets. For protocol bits use masks/shifts over an integer obtained from explicitly parsed bytes.[^iso-c-n1570]

## Detailed explanation

TODO
