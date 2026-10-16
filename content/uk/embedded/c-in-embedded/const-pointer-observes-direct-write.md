---
id: emb-cppfound-0095
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
int x=5;
const int *p=&x;
x=10;
printf("%d",*p);
```

## Short answer

`10`.

`const int *p = &x` – вказівник на const int: забороняє змінювати `*p` (через цей вказівник). Але `x` – не const, тож зміна `x = 10` через пряме ім'я – легальна.

`*p` читає значення `x` = 10. `const` захищає від запису через `p`, але не робить `x` незмінним – це важлива відмінність: `const int *p` vs `const int x`.[^embeddedinterviewlab]

## Detailed explanation

TODO
