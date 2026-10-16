---
id: emb-cppfound-0088
title: "Що виведе?"
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
int a=1,b=2;
int *p=&a,*q=&b;
printf("%d", p<q);
```

## Short answer

<span class="warn">Undefined behavior за стандартом C</span>. Реляційне порівняння (`<`, `>`) вказівників з різних об'єктів не визначено стандартом.

На практиці (більшість платформ, flat memory): результат залежить від розміщення змінних у пам'яті (порядок на стеку залежить від компілятора), тож не portable.

Дозволено: `p == q`, `p != q` – порівняння на рівність між будь-якими вказівниками. Реляційні – тільки в межах одного масиву.[^embeddedinterviewlab]

## Detailed explanation

TODO
