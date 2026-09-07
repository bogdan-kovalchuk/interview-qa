---
id: emb-cppstl-0034
title: "Does `-fno-exceptions` remove the checking code inside `at()` itself?"
description: "No, the bounds check stays; without exceptions the error path often leads to abort or a fatal handler."
track: embedded
section: cpp-embedded-constraints-and-stl
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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

<span class="warn">No – the bounds check stays; in libstdc++-like implementations the error path without exceptions often leads to `abort()`/fatal handler.</span>

That is, the bounds check in `vector::at()`/`array::at()` is still performed; only the reaction to failure changes – an emergency stop without diagnostics instead of an exception.

Protection: for a hot path where the check is redundant, use `operator[]` with your own validation; for safety – log before stopping.[^embeddedinterviewlab]

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
