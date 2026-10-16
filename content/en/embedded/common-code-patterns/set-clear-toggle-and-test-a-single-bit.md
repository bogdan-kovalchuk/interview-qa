---
id: emb-patterns-0014
title: "What do the four basic bit operations look like?"
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
#define BIT32(n) (UINT32_C(1) << (n))
```

## Short answer

**Set / Clear / Toggle / Test:**

```c
reg |=  BIT32(n);   // set
reg &= ~BIT32(n);   // clear
reg ^=  BIT32(n);   // toggle
if (reg & BIT32(n)) { ... } // test
```

Set is OR, clear is AND with the inverted mask, toggle is XOR, test is AND.

`n` must be in the range 0–31 for a 32-bit mask. For a memory-mapped register, check its documentation: ordinary read-modify-write may be unsuitable if the register has special write semantics or is changed by hardware.[^iso-c-n1570]

## Detailed explanation

TODO
