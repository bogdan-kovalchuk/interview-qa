---
id: emb-raii-0009
title: "How do you transfer ownership of a resource through a `unique_ptr`?"
description: "Ownership is transferred via std::move, which leaves the source empty and makes the new owner explicit in the code since uniqueptr is move-only."
track: embedded
section: raii-and-smart-pointers
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

**Via `std::move()` – copying is forbidden, the transfer is explicit.**

`auto b = std::move(a);` moves ownership: `a` becomes empty, `b` now handles the release. This makes ownership visible in the code.

Rule: `unique_ptr` is move-only; an explicit `std::move` documents who owns the resource now.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
