---
id: emb-tmplcx-0014
title: "Where does template code bloat come from?"
description: "Each unique instantiation creates its own definitions of the functions used, usually as separate code in Flash."
track: embedded
section: templates-and-constexpr
level: junior
type: concept
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

<span class="warn">Each unique instantiation creates its own definitions of the functions that are used.</span>[^cpp-draft-temp-inst] In Flash such definitions usually take separate code; the compiler can fold only functions with identical code (in GCC this is `-fipa-icf`).[^gcc-optimize-options]

Example: `CircularBuffer<uint8_t,64>` and `CircularBuffer<uint16_t,64>` give separate sets of the methods the program calls, and their code differs.

Rule: watch the number of instantiations – on flash-constrained MCUs each new type can quickly grow the firmware.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
