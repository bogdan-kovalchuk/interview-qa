---
id: emb-tmplcx-0023
title: "How does a template over a register give compile-time access protection?"
description: "A template can forbid writes to a read-only register or reads from a write-only register at compile time."
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

**A template can forbid writes to a read-only register or reads from a write-only register – at compile time.**

By encoding access rights in the type (e.g. `Register<Addr, ReadOnly>`), an attempt to call `reg.write()` on an RO (read-only) register becomes a compile error. A raw `#define` cannot do that.

Rule: a typed register wrapper catches access errors before the code runs, unlike macros.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
