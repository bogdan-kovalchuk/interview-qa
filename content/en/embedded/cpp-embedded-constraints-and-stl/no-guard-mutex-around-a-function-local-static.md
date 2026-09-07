---
id: emb-cppstl-0020
title: "What does `-fno-threadsafe-statics` do?"
description: "It removes the mutex guard around function-local static initialization."
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

**It removes the mutex guard around function-local static initialization.**

By default the compiler adds a guard (possibly with pthread) so that two threads do not initialize the static simultaneously. On bare metal without threads this is extra code and a dependency.

Rule: `-fno-threadsafe-statics` is appropriate when there is no concurrent access to lazy-init statics (single-threaded bare metal).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
