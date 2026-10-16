---
id: emb-cppfound-0082
title: "What is pointer decay when passing an array as a function argument?"
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

When an array is passed to a function, it **automatically converts** to a pointer to the first element (decay). `int arr[8];` `f(arr)` -> `f(int *)` – the function receives a pointer. Consequences:
- `sizeof(arr)` inside the function = `sizeof(int*)`, not 32;
- No copy – the function accesses the original array;
- No range checking.
Solution: `f(int arr[], size_t n)` or in C++: `template<size_t N> f(int (&arr)[N])`.[^embeddedinterviewlab]

## Detailed explanation

TODO
