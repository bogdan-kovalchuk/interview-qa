---
id: emb-cppfound-0044
title: "Why is `volatile` needed when accessing hardware registers through a pointer?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
---

## Short answer

Without `volatile`, the compiler may:
1. <span class="warn">Cache</span> the register value in a CPU register and not re-read it (missing a hardware change);
2. <span class="warn">Remove "unnecessary" writes</span> (dead store elimination) – if the value is not read later;
3. <span class="warn">Reorder</span> operations for optimization.

With `volatile`: every read/write is actually performed in the order written.

Pattern: `volatile uint32_t * const GPIOA_ODR = (volatile uint32_t*)0x40020014U;`[^embeddedinterviewlab]

## Detailed explanation

TODO
