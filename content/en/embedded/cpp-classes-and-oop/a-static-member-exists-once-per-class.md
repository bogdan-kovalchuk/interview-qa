---
id: emb-cppoop-0028
title: "What is a static class member and where does it live?"
description: "A static member is shared by all instances and lives in data or bss rather than in each object"
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
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

```cpp
class Counter {
  static uint32_t count_; // одна на клас
};
```

## Short answer

**A static member is shared by all instances; it exists in a single copy, not in every object.**

It lives in `.data`/`.bss` (not in the object), so it does not increase `sizeof` the instance. It requires a definition outside the class (pre-C++17) or `inline static`.

Rule: a static member is for class-level data or counters, not per-object data.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
