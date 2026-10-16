---
id: emb-ptrarr-0001
title: "What is the difference between an array's name and a pointer in C, and when do they behave differently?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: c17-standard
    title: "ISO/IEC 9899:2018 (C17 Standard)"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2310.pdf
---

## Short answer

**An array is an object with a fixed element count, whereas a pointer is a separate object storing an address.** In most expressions an array is converted to a pointer to its first element, but not when it is the operand of `sizeof` or unary `&`.[^c17-standard] Therefore `sizeof arr` measures the whole array, while `sizeof ptr` measures the pointer, and `&arr` has pointer-to-array type. Arrays are not assignable, while a non-const pointer is; in a function parameter declaration, however, `int a[]` is adjusted to `int *a`.

## Detailed explanation

TODO
