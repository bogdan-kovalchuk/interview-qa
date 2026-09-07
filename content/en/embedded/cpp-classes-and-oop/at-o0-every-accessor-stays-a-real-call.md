---
id: emb-cppoop-0031
title: "Trap: why do methods inline into bare-metal access only at `-O2` and not at `-O0`?"
description: "At -O0 the compiler does not inline, so every set() becomes a real function call with prologue and epilogue"
track: embedded
section: cpp-classes-and-oop
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

<span class="warn">At `-O0` the compiler does not inline – every `set()` becomes a real function call with prologue/epilogue.</span>

That is, the zero-overhead abstraction only materialises with optimisation enabled; in a debug build the wrapper class costs a function call.

Defence: measure the size/speed of C++ abstractions with release flags (`-O2`/`-Os`), not at `-O0`.[^embeddedinterviewlab]

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
