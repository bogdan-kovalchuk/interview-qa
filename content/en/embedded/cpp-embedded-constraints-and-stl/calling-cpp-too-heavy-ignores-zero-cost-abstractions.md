---
id: emb-cppstl-0026
title: "Trap: why is \"C++ is too heavy for embedded\" a poor answer?"
description: "The claim shows ignorance of zero-cost abstractions and the real levers for controlling runtime overhead."
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

<span class="warn">It demonstrates ignorance of zero-cost abstractions and the real levers for controlling runtime.</span>

Non-virtual classes, templates, `constexpr`, RAII (resource acquisition is initialization) can compile with no extra runtime overhead if you disable/avoid heavy features and check the map file. The real cost depends on the ABI, the standard library and optimizations.

Protection: speak specifically – what exactly you disable (`-fno-exceptions`/`-fno-rtti`) and which subset of the STL you take.[^embeddedinterviewlab]

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
