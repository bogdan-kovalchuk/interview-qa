---
id: emb-cppfound-0027
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
int a=5, b=10;
int *p=&a, *q=&b;
*p=*q;
printf("%d %d",a,b);
```

## Short answer

`a=10, b=10`.

`*p = *q` – копіює **значення** `*q` (тобто `b=10`) у `*p` (тобто у `a`). Самі вказівники `p` і `q` не змінюються.

Якби `p = q` (без *) – обидва вказівники вказували б на `b`, а `a` лишився б `5`.

Типова помилка: плутати присвоєння вказівників та значень.[^embeddedinterviewlab]

## Detailed explanation

TODO
