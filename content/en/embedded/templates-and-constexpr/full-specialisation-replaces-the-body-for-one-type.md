---
id: emb-tmplcx-0009
title: "What is full template specialisation?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-temp-expl-spec
    title: "C++ working draft: Explicit specialization ([temp.expl.spec])"
    url: https://eel.is/c++draft/temp.expl.spec
  - source_id: cpp-draft-temp-spec-partial-general
    title: "C++ working draft: Partial specialization, general ([temp.spec.partial.general])"
    url: https://eel.is/c++draft/temp.spec.partial.general
---

## Question code

```cpp
template<> class SpiDriver<STM32F4> {
  // register layout саме для STM32F4
};
```

## Short answer

**A completely different implementation for a specific type.**

Full specialization is a `template<>` definition that is used instead of the primary template for one set of arguments.[^cpp-draft-temp-expl-spec] It centralizes platform-dependent code in one place instead of scattered `#ifdef` across the project.

Rule: full specialization – for one specific type/platform with a unique implementation.

## Detailed explanation

TODO
