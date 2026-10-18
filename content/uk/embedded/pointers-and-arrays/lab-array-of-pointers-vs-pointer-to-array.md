---
id: emb-cppfound-0065
title: "Яка різниця між `int *arr[5]` і `int (*arr)[5]` у пам'яті?"
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

`int *arr[5]` – масив із 5 вказівників. Розмір: `5 × sizeof(int*) = 20 байт`; кожен з 5 елементів – адреса якогось int, можуть вказувати у різні місця пам'яті.

`int (*arr)[5]` – один вказівник на масив із 5 int. Розмір `arr` = `sizeof(int*) = 4` байти; `arr+1` -> зміщення на `5 × sizeof(int) = 20` байт.

Читай: дужки навколо `*arr` – "вказівник на".[^embeddedinterviewlab]

## Detailed explanation

TODO
