---
id: emb-cppfound-0011
title: "Trap: what happens?"
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

The string literal `"hello"` is stored in **.rodata** (Flash/read-only). `s` points to this read-only region.

Writing `s[0] = 'H'` -> <span class="warn">undefined behavior</span>: on a PC – segfault, on an MCU – HardFault (if MPU protects Flash) or a silent write into Flash (which won't work).

Correct: `char arr[] = "hello";` – the compiler copies the string into a writable array (stack or .data). Then `arr[0] = 'H'` is legal.[^embeddedinterviewlab]

## Detailed explanation

TODO
