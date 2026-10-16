---
id: emb-tmplcx-0010
title: "What is partial template specialisation?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-temp-spec-partial-general
    title: "C++ working draft: Partial specialization, general ([temp.spec.partial.general])"
    url: https://eel.is/c++draft/temp.spec.partial.general
  - source_id: cpp-draft-temp-expl-spec
    title: "C++ working draft: Explicit specialization ([temp.expl.spec])"
    url: https://eel.is/c++draft/temp.expl.spec
---

## Question code

```cpp
template<typename T>
class Buffer<T*> {
  // для всіх вказівникових типів
};
```

## Short answer

**Specialization by pattern (e.g. all pointers), not by a single type.**

`Buffer<T*>` applies to any type of the form `T*` and replaces the primary template only for such arguments.[^cpp-draft-temp-spec-partial-general] Rule: partial specialization – when behavior is common to a whole class of types described by a pattern.

## Detailed explanation

TODO
