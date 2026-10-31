---
id: emb-cppfound-0066
title: "What does this code print?"
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
int a=1;
int *p=&a;
int *q=&a;
q++;
printf("%d",*q);
```

## Short answer

<span class="warn">Undefined behavior</span>. `q++` forms a valid one-past-the-end pointer, but dereferencing `*q` is undefined behavior (UB): scalar `a` is treated as a 1-element array, so no valid element exists past it.

Pointer arithmetic is defined within an array. For separate scalar variables, computing the past-the-end pointer `&a + 1` is valid, but dereferencing `*(&a + 1)` or advancing further is UB. The compiler may also keep `a` in a register without a RAM address, so `*q` reads garbage or causes a fault.[^embeddedinterviewlab]

## Detailed explanation

TODO
