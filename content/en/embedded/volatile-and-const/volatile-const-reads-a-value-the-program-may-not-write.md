---
id: emb-volconst-0014
title: "What is `volatile const` and what is it for?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**`volatile const`** describes an object the program must not modify through this lvalue, but whose value may change without the program's involvement.[^iso-c-n1570]

Typical example: a read-only status register. Firmware only reads; hardware may update the status bits. `volatile` qualifies accesses according to the implementation's rules, while `const` prohibits writes through this type.[^iso-c-n1570]

Embedded rule: for hardware read-only registers, use a pointer to `volatile const` data when that matches the MCU documentation.[^iso-c-n1570]

## Detailed explanation

TODO
