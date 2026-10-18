---
id: emb-cemb-0040
title: "What storage classes exist in C, and how do they relate to linkage and storage duration?"
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

The main specifiers are: `auto`, `register`, `static`, `extern`, `_Thread_local`. `static` at block scope gives static storage duration, and at file scope gives internal linkage. `extern` typically declares an object/function with external linkage, but the lifetime is determined by the object itself, not by the `extern` keyword.[^dou-embedded-interview]

## Detailed explanation

TODO
