---
id: emb-cppfound-0050
title: "Що виведе?"
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

## Question code

```c
int arr[5]={1,2,3,4,5};
int *p=arr;
printf("%d %d", *p++, *p);
```

## Short answer

<span class="warn">Undefined behavior</span> – порядок обчислення аргументів `printf` не визначений стандартом.

`p++` – post-increment: повертає поточне значення і збільшує. Але між обчисленням `*p++` і `*p` в межах одного виклику функції немає sequence point. Компілятор може обчислити аргументи у будь-якому порядку.

Результат залежить від компілятора/платформи. Краще: `printf("%d %d", arr[0], arr[1]);`[^embeddedinterviewlab]

## Detailed explanation

TODO
