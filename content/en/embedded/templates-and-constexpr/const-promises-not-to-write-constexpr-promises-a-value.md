---
id: emb-tmplcx-0007
title: "What is the difference between `const` and `constexpr`?"
description: "const means read-only but the value may be computed at runtime; constexpr means usable as a constant expression."
track: embedded
section: templates-and-constexpr
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

**`const` means "I will not modify it", but the value may be computed at runtime. `constexpr` means "can be a constant expression".**

For embedded, `constexpr` is stronger: it forces initialization to be suitable for compile-time evaluation and for objects with static storage typically leads to ready data in Flash/`.rodata` rather than a startup calculation in RAM.

Rule: for compile-time constants/tables use `constexpr`, not just `const`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
