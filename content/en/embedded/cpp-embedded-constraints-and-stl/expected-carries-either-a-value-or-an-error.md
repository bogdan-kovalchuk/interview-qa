---
id: emb-cppstl-0005
title: "What is `std::expected<T, E>` and what replaces it before C++23?"
description: "A type that carries either a value or an error, making result checking explicit in the type"
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

**A type that carries EITHER a value OR an error, making result checking explicit in the type system.**

Before C++23 you write a lightweight `Result<T, E>` with no heap allocation – a small class with a success/error flag and union-like storage.

Rule: `expected`/`Result` combines value and error in one type, without exceptions and without the heap.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
