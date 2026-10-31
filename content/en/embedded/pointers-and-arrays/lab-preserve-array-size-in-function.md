---
id: emb-cppfound-0062
title: "How can an array be passed to a function while preserving its size?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

Since an array decays to a pointer, the size is <span class="warn">not passed automatically</span>. Options:

1) **Explicit parameter**: `void f(int *arr, size_t n)` – simplest;
2) **Sentinel value**: null-terminator for strings, a special value;
3) **Struct + array**: `struct { int *data; size_t len; }`;
4) C++ **std::span** or `std::array<int,N>`.

Protection: `_Static_assert(sizeof(arr) != sizeof(int*), "Use real array")` at the caller.[^embeddedinterviewlab]

## Detailed explanation

TODO
