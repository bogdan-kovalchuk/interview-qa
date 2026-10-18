---
id: emb-cppfound-0062
title: "Як передати масив у функцію і зберегти інформацію про його розмір?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Оскільки масив decay-ується до вказівника, розмір <span class="warn">не передається автоматично</span>. Варіанти:

1) **Явний параметр**: `void f(int *arr, size_t n)` – найпростіше;
2) **Sentinel value**: null-terminator для рядків, спеціальне значення;
3) **Struct + масив**: `struct { int *data; size_t len; }`;
4) C++ **std::span** або `std::array<int,N>`.

Захист: `_Static_assert(sizeof(arr) != sizeof(int*), "Use real array")` у caller.[^embeddedinterviewlab]

## Detailed explanation

TODO
