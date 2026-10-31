---
id: emb-cppfound-0002
title: "What does this print?"
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

## Question code

```c
int x = 42;
int *p = &x;
printf("%d %p", *p, (void*)p);
```

## Short answer

`*p` -> `42` (dereferencing – reads the value of `x`). `p` -> address of variable `x` (for example, `0x2000FFE0` on the Cortex-M stack).

Key point: `p` and `x` are different objects. `p` holds the address, `x` holds the value. Changing `*p = 100` changes `x`, while changing `p = &y` does not change `x`.[^embeddedinterviewlab]

## Detailed explanation

TODO
