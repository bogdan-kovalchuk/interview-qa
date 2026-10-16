---
id: emb-structs-0020
title: "What is a bit-field in a C struct?"
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

**Bit-field** is a struct or union member with an explicitly specified width in bits, for example `unsigned int mode : 3;`.[^iso-c-n1570]

The implementation places bit-fields in storage units; bit order and fields crossing unit boundaries are implementation-defined. Permitted types are limited by the standard or implementation. This suits compact flags but can be risky for hardware registers and wire formats.[^iso-c-n1570]

For hardware or protocol layouts, rely on bit-fields only when the format and the specific compiler ABI are documented and verified.[^iso-c-n1570]

## Detailed explanation

TODO
