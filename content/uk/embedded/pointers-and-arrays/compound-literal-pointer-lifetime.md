---
id: emb-cppfound-0081
title: "Trap: чи коректно у C99?"
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
int *p = &(int){5};
printf("%d", *p);
```

## Short answer

**Так, коректно** у межах того ж блоку. `(int){5}` – compound literal (C99): тимчасовий об'єкт зі storage duration автоматичного блоку.

<span class="warn">Але dangling pointer</span> якщо вийти за межі блоку: `int *p; { p = &(int){5}; } *p; // UB – блок закінчився`

GCC може не попередити. Безпечне використання: лише у тому ж scope де literal визначений.[^embeddedinterviewlab]

## Detailed explanation

TODO
