---
id: emb-cemb-0012
title: "What is the purpose of the const keyword?"
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

It forbids changing the value through that name after initialization, and a write attempt is a compile error.[^dou-embedded-interview]

Variants: `const int x = 5;` – constant variable; `const int *p` – pointer to constant (data protected); `int * const p` – constant pointer (address protected); `const int * const p` – both protected.

In embedded, `const` guarantees no particular storage location: many toolchains put such data in `.rodata` in Flash, but that depends on the ABI, linker script and platform. On C++ methods, `void get() const` guarantees the method does not change the object's state.

## Detailed explanation

TODO
