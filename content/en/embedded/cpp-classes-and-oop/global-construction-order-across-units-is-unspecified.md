---
id: emb-cppoop-0010
title: "Trap: why is a dependency between globals in different `.cpp` files dangerous?"
description: "The C++ standard does not define construction order of globals across translation units, leading to the static initialization order fiasco."
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

<span class="warn">The C++ standard does not define the construction order of globals across translation units</span> (static initialization order fiasco).

If a global from `a.cpp` uses a global from `b.cpp` in its constructor, the latter may not yet be constructed -> undefined behavior.

Protection: avoid cross-module global dependencies; use function-local static (lazy init on first call) or an explicit init sequence.[^embeddedinterviewlab]

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
