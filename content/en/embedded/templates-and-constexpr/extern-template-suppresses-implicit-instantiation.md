---
id: emb-tmplcx-0016
title: "What does `extern template` do?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-temp-explicit
    title: "C++ working draft: Explicit instantiation ([temp.explicit])"
    url: https://eel.is/c++draft/temp.explicit
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
---

## Question code

```cpp
extern template class Buffer<uint8_t>;
```

## Short answer

**Allows the compiler to skip instantiating the template's members in this translation unit.**[^cpp-draft-temp-explicit] A definition must exist somewhere in the program as an explicit instantiation definition; otherwise the program is ill-formed.[^cpp-draft-temp-explicit] Rule: `extern template` in the header plus one explicit instantiation in one `.cpp` allow avoiding copies in every TU for non-inline members.

## Detailed explanation

TODO
