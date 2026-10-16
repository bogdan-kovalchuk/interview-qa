---
id: emb-tmplcx-0002
title: "How many template instantiations end up in the binary?"
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
---

## Short answer

**One instantiation for each DIFFERENT set of template arguments that is actually used.**

With `max<int>(a, b)` and `max<float>(x, y)` the compiler creates two function instantiations; a function template that is never called is not instantiated.[^cpp-draft-temp-inst]

This counts generated copies of code, not the final flash size: the optimizer may inline calls, so check the result with `nm -C` or the map file.

## Detailed explanation

TODO
