---
id: emb-volconst-0023
title: "What compiles here: `const int * const p`?"
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
const int * const p = &x;
*p = 3;
p = &y;
```

## Short answer

**Neither assignment compiles: `*p = 3` and `p = &y`.**

`const int * const p` means const pointer to const int. Through this pointer, neither the pointed-to value nor the pointer value itself can be changed.

Embedded example: a fixed pointer to a read-only lookup table, or to a read-only register if you add `volatile` for hardware.[^iso-c-n1570]

## Detailed explanation

TODO
