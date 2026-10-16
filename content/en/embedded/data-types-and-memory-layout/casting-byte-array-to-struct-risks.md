---
id: emb-dtypes-0107
title: "What risks arise when casting a byte array to a struct in C?"
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

Casting `uint8_t*` to `struct*` risks violating <span class="warn">alignment</span>, strict aliasing, and the expected layout with padding. The frame may also have a different endianness or packed format than the compiler ABI. It is safer to read fields via `memcpy` into local types, check the length, and explicitly convert byte order.[^iso-c-n1570]

## Detailed explanation

TODO
