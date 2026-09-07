---
id: emb-raii-0015
title: "How do you construct an object without `malloc` in a preallocated buffer?"
description: "Placement new constructs an object in provided memory without allocation."
track: embedded
section: raii-and-smart-pointers
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

```cpp
alignas(T) std::byte storage[sizeof(T)];
T* obj = new (storage) T(args); // placement new
obj->~T(); // явний виклик dtor
```

## Short answer

**Placement new constructs an object in provided memory without allocation.**

The memory can be a static array or a memory pool and must have proper alignment. The destructor must be called explicitly (`obj->~T()`) because `delete` does not apply here.

Rule: placement new plus explicit dtor equals dynamic construction without the heap.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
