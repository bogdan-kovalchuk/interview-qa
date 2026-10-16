---
id: emb-cppstl-0002
title: "Trap: what happens to `throw` and `try`/`catch` under `-fno-exceptions`?"
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

<span class="warn">In your own code `throw`/`try`/`catch` usually become compile errors; library paths that would have thrown an exception often end in `abort()`.</span>

This is not "magic error removal": a path through `vector::at()` out-of-range may crash the system instead of raising a handled exception.

Defence: audit throwing API (application programming interface) in the standard library and replace them with explicit checks/statuses.[^embeddedinterviewlab]

## Detailed explanation

TODO
