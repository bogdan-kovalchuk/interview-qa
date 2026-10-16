---
id: emb-cemb-0025
title: "What are common uses of `extern`?"
track: embedded
section: c-in-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`extern` declares a name that is defined in another translation unit: in a header you write `extern int counter;`, and in one `.c` file there must be a definition `int counter;`. This allows separating declaration and definition without duplicating the global variable.

`extern` is also used for functions, although for ordinary functions external linkage is the default. In C++ there is a special case `extern "C"` – it disables C++ name mangling so that C++ code can link with a C API or a dynamic library.[^dou-embedded-interview]

## Detailed explanation

TODO
