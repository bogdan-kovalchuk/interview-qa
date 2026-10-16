---
id: emb-volconst-0015
title: "Trap: can you write to a register declared like this?"
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

## Question code

```c
volatile const uint32_t * const STATUS =
    (volatile const uint32_t *)0x40020008;

*STATUS = 0;
```

## Short answer

<span class="warn">No. This violates a C language constraint, so the implementation must issue a diagnostic</span>, because `*STATUS` has a const-qualified type.[^iso-c-n1570]

`volatile` does not cancel `const`: it qualifies access to the object, while `const` prohibits modifying it through this lvalue.[^iso-c-n1570]

Fix: declare read-only registers as `volatile const` when that matches the MCU documentation. The standard requires a diagnostic, but the compiler may continue translation after issuing it.[^iso-c-n1570]

## Detailed explanation

TODO
