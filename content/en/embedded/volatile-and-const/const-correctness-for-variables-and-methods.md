---
id: emb-cemb-0015
title: "How is const-correctness for variables handled?"
track: embedded
section: volatile-and-const
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Const-correctness is part of the type, and the compiler checks it on access.[^dou-embedded-interview] A `const` object or parameter forbids writing through that path: `void f(const int *p)` may read `*p`, not modify it.

C++ also applies `const` to methods: `int get() const` means the method does not change the object's logical state. A cast can remove const, but writing to a truly const object is undefined behavior. Put `const` on input the function does not modify.

## Detailed explanation

TODO
