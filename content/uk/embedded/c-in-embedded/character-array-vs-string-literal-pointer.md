---
id: emb-cppfound-0052
title: "Чим відрізняється `char arr[] = \"hello\"` від `char *p = \"hello\"`?"
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

## Short answer

`char arr[] = "hello"` – **масив**: компілятор виділяє 6 байт і копіює символи, дані у writable пам'яті (stack або .data). `arr[0] = 'H'` – легально.

`char *p = "hello"` – **вказівник** на рядковий літерал у .rodata (Flash/read-only). `p[0] = 'H'` -> <span class="warn">UB/HardFault</span>.

`sizeof(arr) = 6`, `sizeof(p) = 4` (або 8) – масив у стеку, вказівник тільки зберігає адресу.[^embeddedinterviewlab]

## Detailed explanation

TODO
