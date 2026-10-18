---
id: emb-cppfound-0042
title: "Яка різниця між масивом вказівників `int *arr[8]` і вказівником на масив `int (*arr)[8]`?"
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

`int *arr[8]` – **масив із 8 вказівників** на int. Розмір: 8 × 4 = 32 байти. Кожен елемент – окрема адреса, може вказувати на різні масиви різних розмірів.

`int (*arr)[8]` – **вказівник на масив** із 8 int; Розмір самого `arr` = 4 байти (вказівник); `arr+1` -> +32 байти (розмір масиву із 8 int).

Пріоритет операторів: `[]` сильніший ніж `*`, тому потрібні дужки.[^embeddedinterviewlab]

## Detailed explanation

TODO
