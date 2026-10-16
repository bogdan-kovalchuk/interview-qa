---
id: emb-tmplcx-0029
title: "How does constexpr give compile-time bounds checking?"
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

**When the size is an NTTP, indices and bounds can be checked with `static_assert` at compile time.**

For example, `get<I>()` with `static_assert(I < N, "out of range")` turns an out-of-bounds access into a compile error instead of a runtime bug.

Rule: move bounds checking into compile time wherever the index or size is statically known.[^embeddedinterviewlab]

## Detailed explanation

TODO
