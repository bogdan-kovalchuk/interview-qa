---
id: emb-cppstl-0027
title: "Why is `<iostream>` avoided in embedded in favour of `printf`?"
description: "iostream pulls in locale support, heap buffers, global initialization and tens of kilobytes of Flash."
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

<span class="warn">`<iostream>` can pull in locale, heap buffers, global initialization and tens of KB of Flash.</span>

`std::cout` initializes heavy infrastructure before `main()`; on an MCU this is often unacceptable. `printf` (especially a trimmed/nano version) or a custom trace backend is usually much lighter.

Rule: for logging on an MCU use `printf` or a custom trace backend, not `iostream`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
