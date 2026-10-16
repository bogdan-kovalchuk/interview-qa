---
id: emb-cppfound-0095
title: "What is printed?"
track: embedded
section: c-in-embedded
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
int x=5;
const int *p=&x;
x=10;
printf("%d",*p);
```

## Short answer

`10`.

`const int *p = &x` – a pointer to const int: it prevents modifying `*p` (through this pointer). But `x` is not const, so changing `x = 10` through the direct name is legal.

`*p` reads the value of `x` = 10. `const` protects against writing through `p`, but does not make `x` immutable – this is an important distinction: `const int *p` vs `const int x`.[^embeddedinterviewlab]

## Detailed explanation

TODO
