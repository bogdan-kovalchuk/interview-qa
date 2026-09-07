---
id: emb-raii-0016
title: "What is a static RAII singleton and when do its constructor and destructor run?"
description: "Function-local static: constructor runs once on first call; destructor is usually registered at program termination."
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

```c
Driver& instance() {
  static Driver d; // ctor - при 1-му виклику
  return d;
}
```

## Short answer

**Function-local static: the constructor runs once on the first call; the destructor is usually registered at program termination.**

This is lazy initialization that avoids the static initialization order fiasco. But in embedded, a function-local static may pull in guard and runtime code for thread-safe initialization; if needed, check `-fno-thread-safe-statics` and the destructor policy.

Rule: Meyers' singleton is heap-free but not always runtime-free; check the generated code for your toolchain.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
