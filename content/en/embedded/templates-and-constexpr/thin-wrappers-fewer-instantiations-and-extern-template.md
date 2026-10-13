---
id: emb-tmplcx-0015
title: "What strategies are there against template code bloat?"
description: "Thin wrapper over `void*`, limiting instantiations, extern template, non-template base, and LTO."
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
  - source_id: cpp-draft-temp-explicit
    title: "C++ working draft: Explicit instantiation ([temp.explicit])"
    url: https://eel.is/c++draft/temp.explicit
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says that an entity with an explicit instantiation declaration that is used in a way that would otherwise cause implicit instantiation must have an explicit instantiation definition somewhere in the program; an explicit instantiation of a class also instantiates its direct non-template members. It does not describe how a compiler avoids copies."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-13
    kind: official
    version: "16.1.0"
    applicability: "Describes -fipa-icf: identical code folding for functions, which reduces code size and works better with link-time optimization; enabled by default at -O2. It does not say which bodies are folded in a particular program."
---

## Short answer

**Thin wrapper over `void*`; limiting the number of instantiations; `extern template`; extracting T-independent code into a non-template base; LTO (link-time optimization).**

Each instantiation with a different `T` creates its own definitions of the functions used,[^cpp-draft-temp-inst] so the shared implementation belongs outside the template. The idea: keep only a thin type-safe layer in the template, and let the logic work through `void*` and the element size or through a base class.

Rule: factor out everything that does not depend on `T` into non-template code.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
