---
id: emb-tmplcx-0017
title: "Trap: why can `std::function` inflate Flash sharply?"
description: "std::function is template-heavy type erasure that can produce a lot of separate code for different signatures."
track: embedded
section: templates-and-constexpr
level: junior
type: pitfall
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

<span class="warn">`std::function` is template-heavy type erasure; different signatures and callable types can produce a lot of separate code.</span>

Each signature is a separate instantiation of the type-erasure machinery, and the implementation may pull in additional runtime code.

Defense: for simple callbacks a function pointer + `void* context` is often sufficient. On flash-constrained MCUs check `std::function` via the linker map.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
