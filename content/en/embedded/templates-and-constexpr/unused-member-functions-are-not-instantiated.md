---
id: emb-tmplcx-0032
title: "Does the compiler generate code for unused member functions of a template?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**Usually no – during implicit instantiation of a class template, only the member functions that are actually needed are generated.**

This limits bloat: if `pop()` is never called on `CircularBuffer<T,N>`, its code typically does not end up in Flash for that instantiation. Exceptions: explicit instantiation, virtual functions, and other ODR-use scenarios can force more code to be generated.

Rule: unused template methods are often free, but check the linker map for template-heavy code.[^embeddedinterviewlab]

## Detailed explanation

TODO
