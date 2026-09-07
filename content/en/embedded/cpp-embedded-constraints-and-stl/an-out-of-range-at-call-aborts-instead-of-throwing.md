---
id: emb-cppstl-0022
title: "Trap: what happens on an out-of-bounds `vector::at()` under `-fno-exceptions`?"
description: "Under -fno-exceptions the out-of-range path ends in abort or another fatal handler instead of throwing."
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
---

## Short answer

<span class="warn">In many embedded toolchains, instead of throwing `std::out_of_range`, the library path ends in `abort()` or another fatal handler.</span>

`-fno-exceptions` does not remove the bounds check; it changes the reaction to failure. On an MCU this often looks like an emergency stop or a HardFault with no proper diagnostics.

Protection: use `std::array` or a custom bounds-checking wrapper that logs data before stopping.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
