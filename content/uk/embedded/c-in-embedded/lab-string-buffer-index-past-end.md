---
id: emb-cppfound-0076
title: "Trap: яка помилка?"
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

## Question code

```c
char buf[4]="abc";
buf[4]='\0';
```

## Short answer

<span class="warn">Buffer overflow!</span> `char buf[4] = "abc"` -> `buf = {'a','b','c','\0'}`. Масив 4 елементи, індекси 0..3, а `buf[4]` – п'ятий елемент, за межами масиву.

Ще проблема: `"abc"` вже має '\0' на позиції 3 – null-terminator вже є, тож рядок коректний.

Якби `char buf[3] = "abc"` – компілятор попередить або поміщає 'a','b','c' без '\0' (усікання); Завжди розмір буфера > довжина рядка + 1.[^embeddedinterviewlab]

## Detailed explanation

TODO
