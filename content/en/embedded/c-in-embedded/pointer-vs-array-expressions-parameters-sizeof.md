---
id: emb-cemb-0034
title: "How does a pointer differ from an array in expressions, function parameters, and sizeof?"
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

An array is an object with N elements; in most expressions it decays to a pointer to the first element. In a function parameter, `int a[]` is actually `int *a`, so the length is not passed automatically. `sizeof array` in the same scope gives the full size of the array, while `sizeof pointer` gives only the size of the address.[^dou-embedded-interview]

## Detailed explanation

TODO
