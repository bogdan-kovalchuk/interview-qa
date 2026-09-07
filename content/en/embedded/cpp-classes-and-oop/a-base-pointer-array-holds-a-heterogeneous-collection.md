---
id: emb-cppoop-0019
title: "What is polymorphism through a `Sensor*` array for?"
description: "A heterogeneous collection of different concrete types behind a common interface in one array or container"
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

## Short answer

**A heterogeneous collection: different concrete types behind a common interface in one array/container.**

```c
Sensor* arr[] = { &temp, &pressure, &humid };
for (auto s : arr) s->read();
```

The call through a base pointer picks the implementation at runtime via the vtable.

Rule: when you need to hold DIFFERENT types together and call them uniformly, this is the primary use case for virtual.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
