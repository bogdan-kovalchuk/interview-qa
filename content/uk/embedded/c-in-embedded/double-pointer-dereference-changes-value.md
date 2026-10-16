---
id: emb-cppfound-0045
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
int x=10;
int *p=&x;
int **pp=&p;
**pp=20;
printf("%d",x);
```

## Short answer

`20`.

Ланцюжок: `pp` -> `&p` (адреса вказівника `p`), `*pp` -> розіменування = сам вказівник `p` (адреса `x`), `**pp` -> подвійне розіменування = значення `x`.

`**pp = 20` -> запис 20 у `x` через ланцюжок, тож `x` стає 20. Всі три: `x`, `*p`, `**pp` тепер = 20.[^embeddedinterviewlab]

## Detailed explanation

TODO
