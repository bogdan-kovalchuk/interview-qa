---
id: emb-cppstl-0006
title: "Which allocation strategies are used instead of the heap?"
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

**Static allocation, placement new, fixed-size memory pools, stack allocation.**

All objects have static/automatic storage; there is no `new`/`delete`. A pool gives O(1) with no fragmentation; the stack is for locals, but small (stacks 1–4 KB).

Rule: in safety-critical embedded the heap is either forbidden or used only during initialisation.[^embeddedinterviewlab]

## Detailed explanation

TODO
