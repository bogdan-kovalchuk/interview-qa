---
id: emb-cemb-0003
title: "What pointer operations are there?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Main operations: take the address `&x`, dereference `*p`, access a field via `p->field`, compare with `NULL` or another pointer, assign an address, cast the type, pass to a function.[^dou-embedded-interview]

There is pointer arithmetic: `p + 1` advances not by 1 byte but by `sizeof(*p)` bytes. So for `int *p`, `p++` shifts by the size of `int`. Correct arithmetic is defined within a single array or one past its end; going out of bounds and dereferencing an invalid address is undefined behavior.

## Detailed explanation

TODO
