---
id: emb-cppfound-0048
title: "Що поверне на 32-bit?"
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
char *p = "hello";
printf("%zu", sizeof(p));
```

## Short answer

**4** (на 64-bit – 8).

`p` – вказівник типу `char*`, тож `sizeof(p) = sizeof(char*) = 4` на 32-bit. Не розмір рядка, не 6 (з '\0'), а лише розмір вказівника.

Для розміру рядка: `strlen(p) + 1` = 6 (з null-terminator) або `strlen(p)` = 5.

Порівняй: `char arr[] = "hello"; sizeof(arr) = 6` – тут масив, не вказівник.[^embeddedinterviewlab]

## Detailed explanation

TODO
