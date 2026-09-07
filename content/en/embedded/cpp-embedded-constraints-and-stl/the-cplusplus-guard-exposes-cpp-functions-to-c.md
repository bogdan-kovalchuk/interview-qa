---
id: emb-cppstl-0016
title: "How do you expose C++ functions for calling from C?"
description: "An #ifdef cplusplus guard enables extern \"C\" only for the C++ compiler."
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

```c
#ifdef __cplusplus
extern "C" {
#endif
  void app_init(void);
#ifdef __cplusplus
}
#endif
```

## Short answer

**The `#ifdef __cplusplus` guard enables `extern "C"` only for the C++ compiler.**

A C compiler does not understand the `extern "C"` syntax (it is a C++ keyword); the guard lets a single header work in both languages.

Rule: shared headers must always have an `#ifdef __cplusplus` guard around `extern "C"`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
