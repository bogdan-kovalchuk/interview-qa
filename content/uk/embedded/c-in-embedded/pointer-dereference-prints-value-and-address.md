---
id: emb-cppfound-0002
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
int x = 42;
int *p = &x;
printf("%d %p", *p, (void*)p);
```

## Short answer

`*p` -> `42` (розіменування – читає значення `x`). `p` -> адреса змінної `x` (наприклад, `0x2000FFE0` на стеку Cortex-M).

Важливо: `p` і `x` – різні об'єкти. `p` зберігає адресу, `x` – значення. Зміна `*p = 100` змінює `x`, а зміна `p = &y` не змінює `x`.[^embeddedinterviewlab]

## Detailed explanation

TODO
