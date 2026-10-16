---
id: emb-cppstl-0020
title: "What does `-fno-threadsafe-statics` do?"
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

**It removes the mutex guard around function-local static initialization.**

By default the compiler adds a guard (possibly with pthread) so that two threads do not initialize the static simultaneously. On bare metal without threads this is extra code and a dependency.

Rule: `-fno-threadsafe-statics` is appropriate when there is no concurrent access to lazy-init statics (single-threaded bare metal).[^embeddedinterviewlab]

## Detailed explanation

TODO
