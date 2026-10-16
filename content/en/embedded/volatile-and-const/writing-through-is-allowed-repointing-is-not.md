---
id: emb-volconst-0022
title: "What compiles here: `int * const p`?"
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
int x = 1, y = 2;
int * const p = &x;
*p = 3;
p = &y;
```

## Short answer

**`*p = 3` compiles, `p = &y` does not compile.**

`int * const p` means const pointer to int. The address stored in `p` is immutable, but the object `x` itself is mutable.

Rule: if `const` is to the right of `*`, the pointer is protected; if to the left of `*`, the data is protected.[^iso-c-n1570]

## Detailed explanation

TODO
