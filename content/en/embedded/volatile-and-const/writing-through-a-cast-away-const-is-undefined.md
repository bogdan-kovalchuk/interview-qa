---
id: emb-volconst-0032
title: "Trap: is it safe to cast `const` away?"
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
const uint32_t cfg = 10;
uint32_t *p = (uint32_t *)&cfg;
*p = 20;
```

## Short answer

<span class="warn">No: if the original object was declared `const`, attempting to modify it through a non-const lvalue has undefined behavior.</span>

On an MCU, `cfg` may reside in Flash/`.rodata`, and a write through `p` can cause a BusFault/HardFault or simply leave the data unchanged. Even if the address is in RAM, the optimizer may assume that `cfg` does not change.

Protection: do not cast away `const` for writing. If the data must change, it must not be `const`.[^iso-c-n1570]

## Detailed explanation

TODO
