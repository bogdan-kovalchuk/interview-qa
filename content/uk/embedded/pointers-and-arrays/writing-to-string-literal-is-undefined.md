---
id: emb-cppfound-0011
title: "Trap: що станеться?"
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
char *s = "hello";
s[0] = 'H';
```

## Short answer

Рядковий літерал `"hello"` зберігається у **.rodata** (Flash/read-only). `s` вказує на цю read-only область.

Запис `s[0] = 'H'` -> <span class="warn">undefined behavior</span>: на ПК – segfault, на MCU – HardFault (якщо MPU захищає Flash) або тихий запис у Flash (що не спрацьовує).

Правильно: `char arr[] = "hello";` – компілятор копіює рядок у writable масив (stack або .data). Тоді `arr[0] = 'H'` – легально.[^embeddedinterviewlab]

## Detailed explanation

TODO
