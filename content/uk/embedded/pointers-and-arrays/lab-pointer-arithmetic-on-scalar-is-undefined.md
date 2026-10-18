---
id: emb-cppfound-0066
title: "Trap: що виведе?"
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
int a=1;
int *p=&a;
int *q=&a;
q++;
printf("%d",*q);
```

## Short answer

<span class="warn">Undefined behavior</span>. `q++` -> `q` тепер вказує на адресу одразу після `a` на стеку, а це не елемент масиву – лише окрема змінна.

Pointer arithmetic визначена тільки в межах масиву (або struct за умовами). Для двох окремих змінних – навіть якщо вони поруч на стеку – `&a + 1` -> UB.

Компілятор може розмістити `a` у регістрі без адреси у пам'яті -> `*q` читає сміття.[^embeddedinterviewlab]

## Detailed explanation

TODO
