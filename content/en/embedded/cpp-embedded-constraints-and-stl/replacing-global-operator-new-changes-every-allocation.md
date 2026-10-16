---
id: emb-cppstl-0008
title: "Trap: why is overriding the global `operator new` with a pool allocator dangerous?"
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

<span class="warn">It silently changes the semantics of EVERY allocation, including third-party libraries.</span>

Any code that calls `new` anywhere inside (even library code) will suddenly go through your pool – with unpredictable consequences for size/timing.

Defence: it is safer to `= delete` the global `operator new` entirely, so that an accidental heap allocation becomes a compile error.[^embeddedinterviewlab]

## Detailed explanation

TODO
