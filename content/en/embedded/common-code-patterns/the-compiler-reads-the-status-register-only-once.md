---
id: emb-patterns-0025
title: "Trap: why does this polling loop become endless without `volatile`?"
track: embedded
section: common-code-patterns
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
while (!(REG->SR & FLAG))
    ;
```

## Short answer

<span class="warn">The compiler reads `SR` once, sees the flag is not set, and never re-reads it</span> – in the C abstract machine nothing changes `SR`.

Result: the loop spins on the cached value forever, even after the hardware has already set the flag.

Defense: declare the register `volatile` so accesses remain observable in the C abstract machine; this does not replace synchronization between threads or an ISR.[^iso-c-n1570]

## Detailed explanation

TODO
