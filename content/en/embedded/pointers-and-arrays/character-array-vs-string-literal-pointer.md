---
id: emb-cppfound-0052
title: "What is the difference between `char arr[] = \"hello\"` and `char *p = \"hello\"`?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
---

## Short answer

`char arr[] = "hello"` is an **array**: the compiler allocates 6 bytes and copies the characters; the data resides in writable memory (stack or .data). `arr[0] = 'H'` is legal.

`char *p = "hello"` is a **pointer** to a string literal in .rodata (Flash/read-only). `p[0] = 'H'` -> <span class="warn">UB/HardFault</span>.

`sizeof(arr) = 6`, `sizeof(p) = 4` (or 8) – the array is on the stack, the pointer only holds the address.[^embeddedinterviewlab]

## Detailed explanation

TODO
