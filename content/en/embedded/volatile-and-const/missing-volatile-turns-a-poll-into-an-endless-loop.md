---
id: emb-volconst-0005
title: "What can happen to this loop without `volatile`?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-volatile
    title: "GCC documentation: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
---

## Question code

```c
uint8_t flag = 0;

while (flag == 0) {
    /* flag встановлює ISR */
}
```

## Short answer

If an ISR changes this object asynchronously without informing the compiler, the loop may become <span class="warn">infinite</span>: ordinary C code does not change `flag`.

The optimiser may read `flag` once and reuse it even if the ISR changes memory.[^iso-c-n1570]

Mitigation: declare the flag as `volatile uint8_t flag` if required by your toolchain's ISR model. If atomicity or ordering of other data matters, add an appropriate critical section or atomic/barrier API.[^iso-c-n1570] [^gcc-volatile]

## Detailed explanation

TODO
