---
id: emb-volconst-0013
title: "What does `volatile const uint32_t * const STATUS` mean?"
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

**`STATUS` is a const pointer to volatile const `uint32_t`**.

The pointer address does not change. Writes through this type are not permitted, while the volatile qualifier applies to accesses to the target object; the C implementation defines the precise access rules. This is a typical type for a read-only status register when that matches the MCU documentation.[^iso-c-n1570]

Rule: `const` prevents modification through this lvalue, while `volatile` qualifies an object that may change in ways unknown to the implementation.[^iso-c-n1570]

## Detailed explanation

TODO
