---
id: emb-tmplcx-0015
title: "What strategies are there against template code bloat?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
  - source_id: cpp-draft-temp-explicit
    title: "C++ working draft: Explicit instantiation ([temp.explicit])"
    url: https://eel.is/c++draft/temp.explicit
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
---

## Short answer

**Thin wrapper over `void*`; limiting the number of instantiations; `extern template`; extracting T-independent code into a non-template base; LTO (link-time optimization).**

Each instantiation with a different `T` creates its own definitions of the functions used,[^cpp-draft-temp-inst] so the shared implementation belongs outside the template. The idea: keep only a thin type-safe layer in the template, and let the logic work through `void*` and the element size or through a base class.

Rule: factor out everything that does not depend on `T` into non-template code.[^embeddedinterviewlab]

## Detailed explanation

TODO
