---
id: emb-cppstl-0034
title: "Does `-fno-exceptions` remove the checking code inside `at()` itself?"
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

<span class="warn">No – the bounds check stays; in libstdc++-like implementations the error path without exceptions often leads to `abort()`/fatal handler.</span>

That is, the bounds check in `vector::at()`/`array::at()` is still performed; only the reaction to failure changes – an emergency stop without diagnostics instead of an exception.

Protection: for a hot path where the check is redundant, use `operator[]` with your own validation; for safety – log before stopping.[^embeddedinterviewlab]

## Detailed explanation

TODO
