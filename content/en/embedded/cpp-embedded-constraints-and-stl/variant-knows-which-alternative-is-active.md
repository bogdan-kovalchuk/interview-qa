---
id: emb-cppstl-0032
title: "What is `std::variant` and how is it better than a union?"
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

**A type-safe union (C++17): it knows which type is currently active and does not let you read a different one.**

A raw `union` does not track the active member – reading the "wrong" field is undefined behavior. `std::variant` + `std::visit` make this safe, without the heap.

Protection: the visitor must cover all alternatives; an incorrect visitor is usually caught at compile time, not at runtime.[^embeddedinterviewlab]

## Detailed explanation

TODO
