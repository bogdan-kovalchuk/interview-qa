---
id: emb-cppstl-0018
title: "Trap: what happens to a shared header without an `#ifdef __cplusplus` guard?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">A C compiler encounters `extern "C"` and fails with a syntax error</span> – this is a C++ construct unknown to C.

A header meant for both languages will break the C build without a guard.

Protection: always wrap `extern "C" { ... }` in `#ifdef __cplusplus ... #endif` on both ends.[^embeddedinterviewlab]

## Detailed explanation

TODO
