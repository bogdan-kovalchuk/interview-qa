---
id: emb-cppstl-0005
title: "What is `std::expected<T, E>` and what replaces it before C++23?"
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

**A type that carries EITHER a value OR an error, making result checking explicit in the type system.**

Before C++23 you write a lightweight `Result<T, E>` with no heap allocation – a small class with a success/error flag and union-like storage.

Rule: `expected`/`Result` combines value and error in one type, without exceptions and without the heap.[^embeddedinterviewlab]

## Detailed explanation

TODO
