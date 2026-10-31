---
id: emb-cemb-0022
title: "How does `const` affect a variable?"
track: embedded
section: volatile-and-const
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

`const` sets read-only semantics for the compiler: after initialization the object cannot be modified through the const-qualified name, as in `const int x = 5;`. It does not guarantee the data sits in Flash or ROM; placement depends on toolchain, linker script and platform.

Read pointers right to left: `const int *p` – pointer to constant data; `int * const p` – constant pointer; `const int * const p` – both. `const` is not always a compile-time constant and a cast can remove it, but writing to a truly const object is undefined behavior.[^dou-embedded-interview]

## Detailed explanation

TODO
