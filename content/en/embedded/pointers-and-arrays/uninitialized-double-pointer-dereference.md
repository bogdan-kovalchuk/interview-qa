---
id: emb-cppfound-0096
title: "Trap: what is wrong?"
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
int **pp;
*pp = malloc(10*sizeof(int));
```

## Short answer

<span class="warn">Wild pointer – UB.</span> `int **pp;` – an uninitialized double pointer, contains a garbage address.

`*pp = malloc(...)` – dereferences `pp` (UB!) and writes the allocated memory address to an unknown location. This can corrupt any memory region.

Correct:

```c
int *p = NULL;
int **pp = &p;
*pp = malloc(10*sizeof(int));
```

Always initialize pointers before use.[^embeddedinterviewlab]

## Detailed explanation

TODO
