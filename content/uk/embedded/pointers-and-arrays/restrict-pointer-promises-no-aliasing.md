---
id: emb-cppfound-0028
title: "Що таке `restrict` і навіщо він потрібен у embedded?"
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

`restrict` (C99) – кваліфікатор вказівника, що гарантує компілятору: через цей вказівник і через жоден інший вказівник у цій функції **не відбувається aliasing** (перекриття областей пам'яті).

Приклад: `void add(int * restrict dst, const int * restrict src, int n)`.

Дає компілятору дозвіл на агресивну оптимізацію (векторизація, підкачка у регістри). Важливо для DSP, crypto, memcpy-like функцій. Якщо aliasing все ж є – undefined behavior (UB).[^embeddedinterviewlab]

## Detailed explanation

TODO
