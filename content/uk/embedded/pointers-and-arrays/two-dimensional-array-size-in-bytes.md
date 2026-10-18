---
id: emb-cppfound-0024
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
int arr[3][4];
printf("%zu", sizeof(arr));
```

## Short answer

**48** байт.

`arr` – 2D масив: 3 рядки × 4 стовпці × `sizeof(int) = 4` байти = 48B.

`sizeof(arr[0])` = `sizeof(int[4])` = 16B (один рядок), `sizeof(arr[0][0])` = `sizeof(int)` = 4B.

Кількість рядків: `sizeof(arr)/sizeof(arr[0]) = 48/16 = 3`. Цей трюк працює лише у тому ж scope де оголошений масив.[^embeddedinterviewlab]

## Detailed explanation

TODO
