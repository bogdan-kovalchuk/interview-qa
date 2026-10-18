---
id: emb-cppfound-0003
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
int *p;
*p = 5;
```

## Short answer

`p` is a <span class="warn">wild pointer</span>: an uninitialized pointer holds a garbage address (a random value from the stack).

Writing `*p = 5` -> undefined behavior: it may overwrite a random memory region, another variable, or cause a <span class="warn">HardFault</span> on Cortex-M (if the address is outside RAM).

Protection: always initialize pointers: `int *p = NULL;` or immediately `int *p = &x;`[^embeddedinterviewlab]

## Detailed explanation

TODO
