---
id: emb-volconst-0047
title: "What does `const volatile` mean for a memory-mapped device ID register?"
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

**`const volatile` forbids writes through this lvalue while retaining volatile access semantics.**

A device ID can be read-only from firmware's perspective, while its value is supplied by hardware. `const` and `volatile` describe different access properties; they do not guarantee physical immutability or specific device behaviour.[^iso-c-n1570]

Use `const volatile` for a memory-mapped register only when the MCU documentation defines it as read-only.[^iso-c-n1570]

## Detailed explanation

TODO
