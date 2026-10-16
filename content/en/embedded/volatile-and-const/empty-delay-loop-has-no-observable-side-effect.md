---
id: emb-volconst-0034
title: "Trap: what is wrong with this delay loop?"
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
for (uint32_t i = 0; i < 100000; ++i) {
}
```

## Short answer

<span class="warn">The compiler can remove an empty loop entirely</span> because it has no observable side effects.[^iso-c-n1570]

Adding `volatile` to the counter sometimes forces the increments to execute, but this is a poor basis for accurate timing: optimization level, CPU frequency, wait states, and pipeline all change the real delay.

Protection: for delays, use a hardware timer, SysTick, DWT cycle counter, or RTOS delay. `volatile` is not a timing API.[^iso-c-n1570]

## Detailed explanation

TODO
