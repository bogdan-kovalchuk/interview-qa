---
id: emb-cppstl-0018
title: "Trap: what happens to a shared header without an `#ifdef __cplusplus` guard?"
description: "A C compiler hits extern \"C\" and fails with a syntax error because it is a C++ construct."
track: embedded
section: cpp-embedded-constraints-and-stl
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

<span class="warn">A C compiler hits `extern "C"` and fails with a syntax error</span> – this is a C++ construct unknown to C.

A header intended for both languages, without the guard, breaks the C build.

Protection: always wrap `extern "C" { ... }` in `#ifdef __cplusplus ... #endif` on both sides.[^embeddedinterviewlab]

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
