---
id: emb-cppoop-0008
title: "Trap: when do global constructors run and what must startup do?"
description: "Global constructors run before main via .initarray; bare-metal startup must walk it or objects stay unconstructed."
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

<span class="warn">Global constructors run before `main()` via the `.init_array` section.</span>

On bare metal, startup code must manually walk `.init_array` and call each constructor; otherwise global objects remain only zero-initialized, not constructed (for a polymorphic object this may mean an incorrect vptr).

Protection: make sure startup iterates `.init_array` before `main()`; this is a common bug when porting C++ to bare metal.[^embeddedinterviewlab]

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
