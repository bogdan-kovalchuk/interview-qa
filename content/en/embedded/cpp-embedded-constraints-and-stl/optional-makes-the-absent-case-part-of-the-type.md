---
id: emb-cppstl-0012
title: "How is `std::optional<T>` better than a null pointer?"
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

**It stores the value inline (no heap) and makes the "no value" case explicit in the type system.**

This reduces the risk of null dereference: before accessing `*opt` you must check `opt.has_value()`. For example, `std::optional<FaultCode>` expresses "fault present/absent" better than null signalling.

Rule: for "a value may be absent" use `std::optional`, not a sentinel/null pointer.[^embeddedinterviewlab]

## Detailed explanation

TODO
