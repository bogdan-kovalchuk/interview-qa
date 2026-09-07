---
id: emb-cppstl-0033
title: "What does a typical embedded C++ compile line look like?"
description: "A typical line combines -Os for size optimization with -fno- flags and -std=c++17 for deterministic bare-metal code."
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: mechanism
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

## Question code

```text
arm-none-eabi-g++ -mcpu=cortex-m4 -mthumb -Os \
  -fno-exceptions -fno-rtti -fno-threadsafe-statics \
  -fno-use-cxa-atexit -fno-unwind-tables \
  -std=c++17 -Wall -Werror
```

## Short answer

**`-Os` (size optimization) + a set of `-fno-*` flags that strip C++-runtime-heavy features + `-std=c++17`.**

This gives compact, deterministic code without exceptions, RTTI, unwind tables or thread-safe static guards.

Rule: know these flags by heart – a typical expectation at an embedded C++ interview.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
