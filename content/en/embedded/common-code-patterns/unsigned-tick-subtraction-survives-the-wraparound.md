---
id: emb-patterns-0037
title: "How do you add a timeout to a flag-polling loop?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: holzmann-power-of-ten
    title: "The Power of Ten – Rules for Developing Safety Critical Code (G. J. Holzmann, NASA/JPL)"
    url: https://spinroot.com/gerard/pdf/P10.pdf
---

## Question code

```c
uint32_t start = tick();
while (!(REG->SR & FLAG)) {
  if (tick() - start > TIMEOUT_MS) return ERR_TIMEOUT;
}
```

## Short answer

**Record the start tick and compare the difference `tick() - start` with the limit on every iteration.**

Unsigned subtraction gives the correct elapsed time even after the counter wraps, provided `tick()` returns the same unsigned type as `start` and the wait is shorter than the counter period.[^iso-c-n1570] This keeps the loop from hanging forever if the hardware never sets the flag: after the timeout, return an error instead of waiting.[^holzmann-power-of-ten]

## Detailed explanation

TODO
