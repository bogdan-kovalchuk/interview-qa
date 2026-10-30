---
id: emb-cemb-0002
title: "How do you work with `void`?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

`void` means "absence of type". Three uses:

1. **Function with no return**: `void init(void);`
2. **Function with no parameters**: `int get(void);` – in C, `int f()` and `int f(void)` differ!
3. **Generic pointer**: `void *ptr` – a pointer to any object type; it cannot be directly dereferenced or used in standard pointer arithmetic.

In C, `void *` implicitly converts to an object pointer, but before access you need a concrete type: `int *p = ptr;`. In C++ such a conversion requires an explicit cast.[^dou-embedded-interview]

## Detailed explanation

TODO
