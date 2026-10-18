---
id: emb-cemb-0007
title: "How are parameters passed to a function?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

In C, parameters are passed **by value**: the function receives a copy of the argument.[^dou-embedded-interview] If you pass `int x`, modifying the parameter inside the function does not change the caller's variable.

To let a function modify an object or avoid copying a large one, pass its address: `void f(int *p)` or `void g(struct Big *s)`. Arrays in parameters actually decay to a pointer to the first element, so the array size must be passed separately. In C++ there are also references: `T&` and `const T&`.

## Detailed explanation

TODO
