---
id: emb-tmplcx-0013
title: "Trap: why can you not say \"templates are free\"?"
description: "Templates may have zero runtime cost but real cost in Flash and compile time."
track: embedded
section: templates-and-constexpr
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-13
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-13; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says that a function template or member function specialization is instantiated when its definition is needed; implicit instantiation of a class template instantiates only the member declarations. It says nothing about code size."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-13
    kind: official
    version: "16.1.0"
    applicability: "Describes -fipa-icf: identical code folding for functions, which reduces code size and works better with link-time optimization; enabled by default at -O2. It does not say which bodies are folded in a particular program."
---

## Short answer

<span class="warn">Templates may have zero runtime cost, but they have real cost in Flash and compile time.</span>

Each used function specialization is instantiated when its definition is needed,[^cpp-draft-temp-inst] and its code can take its own space in Flash; the build spends time on instantiation and type checking.

Defense: in an interview say "zero runtime cost does not mean zero flash cost", and check the linker map.[^embeddedinterviewlab]

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
