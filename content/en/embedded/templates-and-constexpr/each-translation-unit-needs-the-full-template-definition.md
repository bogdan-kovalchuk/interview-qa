---
id: emb-tmplcx-0028
title: "Why are templates usually header-only?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**The compiler needs the full definition of a template in every TU (translation unit) to instantiate it for specific types.**

If the definition is hidden in a `.cpp`, other translation units cannot generate the required instantiation -> linker error. That is why templates go into headers.

Rule: template definitions belong in headers; use `extern template` to control instantiation.[^embeddedinterviewlab]

## Detailed explanation

TODO
