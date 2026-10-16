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
---

## Short answer

<span class="warn">A C compiler hits `extern "C"` and fails with a syntax error</span> – this is a C++ construct unknown to C.

A header intended for both languages, without the guard, breaks the C build.

Protection: always wrap `extern "C" { ... }` in `#ifdef __cplusplus ... #endif` on both sides.[^embeddedinterviewlab]

## Detailed explanation

TODO
