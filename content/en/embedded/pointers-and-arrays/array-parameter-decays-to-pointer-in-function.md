---
id: emb-cppfound-0006
title: "Trap: why does sizeof(arr) in a function return 4 or 8 instead of the array size?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-warning-options
    title: "GCC 16.1.0: Warning Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Warning-Options.html
---

## Short answer

When an array is passed to a function, it <span class="warn">decays to a pointer</span>: `void f(int arr[])` ≡ `void f(int *arr)`.

`sizeof(arr)` inside the function = `sizeof(int*)` = 4 or 8 (pointer size), not the array size.

Real case: changed `int16_t buffer[256]` to `int16_t *buffer` but kept `sizeof(buffer)/sizeof(buffer[0])` -> processed only 2 elements instead of 256.

Solution: pass the size explicitly: `void f(int *arr, size_t n)`.[^embeddedinterviewlab]

## Detailed explanation

TODO
