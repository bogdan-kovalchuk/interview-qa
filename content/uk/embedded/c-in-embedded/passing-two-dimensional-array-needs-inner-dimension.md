---
id: emb-cppfound-0029
title: "Як правильно передати 2D масив у функцію та звернутись до елемента `[2][3]`?"
track: embedded
section: c-in-embedded
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Для статично розмірного масиву потрібно вказати **розмір внутрішнього виміру**: `void f(int arr[][4], int rows) { arr[2][3] = 99; }` або еквівалентно: `void f(int (*arr)[4], int rows) { ... }`

Без розміру компілятор не знає крок рядка (stride). `arr[i][j]` -> `*(*(arr+i)+j)` -> в пам'яті: `arr + i*4*sizeof(int) + j*sizeof(int)`.

Для динамічного: передавай як `int *` і обчислюй offset вручну.[^embeddedinterviewlab]

## Detailed explanation

TODO
