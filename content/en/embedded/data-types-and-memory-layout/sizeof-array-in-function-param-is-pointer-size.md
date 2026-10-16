---
id: emb-dtypes-0036
title: "Trap: where does the `sizeof(arr)/sizeof(arr[0])` trick fail?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

In a function parameter, `int arr[]` is adjusted to `int *arr`, so `sizeof(arr)` gives the pointer size, not the array size; its exact value is implementation-dependent.[^iso-c-n1570] Dividing by `sizeof(arr[0])` does not recover the element count. Pass the length separately or use a container that retains it, such as `std::array` or `std::span` in C++.[^iso-c-n1570]

## Detailed explanation

TODO
