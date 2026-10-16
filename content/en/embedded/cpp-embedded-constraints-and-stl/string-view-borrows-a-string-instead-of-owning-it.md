---
id: emb-cppstl-0013
title: "Why is `std::string_view` safer for embedded while `std::string` is risky?"
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

**`string_view` is a non-owning, zero-copy view over a string with no allocation; `std::string` usually owns a buffer and may allocate on the heap.**

`string_view` stores only a pointer + length, does not copy data and does not require a null-terminated string. This is convenient for parsers and logs without the heap.

Defence: `string_view` does not extend lifetime – make sure the source string outlives the view.[^embeddedinterviewlab]

## Detailed explanation

TODO
