---
id: emb-cppstl-0030
title: "How does a compile-time ban on the heap help auditing safety-critical code?"
description: "Deleting or blocking the global operator new turns accidental heap allocation into a compile or link error."
track: embedded
section: cpp-embedded-constraints-and-stl
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

**If the global `operator new` is deleted or blocked, an accidental heap allocation becomes a compile/link error.**

Objects can be built via placement new in statically allocated buffers or fixed-capacity pools. This is easier to argue in a memory-safety review than a policy of "just do not use the heap".

Rule: `= delete` on the global `new` turns a no-heap policy from discipline into a structural guarantee.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
