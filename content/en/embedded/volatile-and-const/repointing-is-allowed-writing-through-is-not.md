---
id: emb-volconst-0021
title: "What compiles here: `const int *p`?"
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
const int *p = &x;
p = &y;
*p = 3;
```

## Short answer

**`p = &y` compiles, `*p = 3` does not compile.**

`const int *p` means pointer to const int. Const applies to the data pointed to by `p`, not to the pointer itself. So the pointer can be changed, but writing through it is forbidden.

Rule: if `const` is to the left of `*`, the pointed-to data is protected.[^iso-c-n1570]

## Detailed explanation

TODO
