---
id: emb-cppfound-0031
title: "Як пов'язані `arr[i]` і `*(arr+i)` за стандартом C?"
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

За стандартом C (§6.5.2.1): **`arr[i]` визначається як `*(arr+i)`**. Це не синтаксичний цукор – це точне визначення subscript operator.

Наслідки:
- `arr[2] == *(arr+2) == *(2+arr) == 2[arr]` – всі еквівалентні;
- Індексування – просто pointer arithmetic + dereference;
- Від'ємні індекси (`arr[-1]`) формально дозволені якщо вказівник вже зсунутий і результат вказує у межах масиву.[^embeddedinterviewlab]

## Detailed explanation

TODO
