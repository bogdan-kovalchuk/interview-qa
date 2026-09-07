---
id: emb-cppstl-0013
title: "Why is `std::string_view` safer for embedded while `std::string` is risky?"
description: "stringview is a non-owning zero-copy view with no allocation while std::string may use the heap"
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

**`string_view` is a non-owning, zero-copy view over a string with no allocation; `std::string` usually owns a buffer and may allocate on the heap.**

`string_view` stores only a pointer + length, does not copy data and does not require a null-terminated string. This is convenient for parsers and logs without the heap.

Defence: `string_view` does not extend lifetime – make sure the source string outlives the view.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
