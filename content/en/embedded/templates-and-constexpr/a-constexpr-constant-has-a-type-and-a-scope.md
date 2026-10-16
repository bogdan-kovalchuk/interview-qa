---
id: emb-tmplcx-0008
title: "Why is a `constexpr` variable better than a `#define` constant?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-cpp-replace
    title: "C++ working draft: Replacement of macros ([cpp.replace])"
    url: https://eel.is/c++draft/cpp.replace
  - source_id: cpp-draft-lex-phases
    title: "C++ working draft: Phases of translation ([lex.phases])"
    url: https://eel.is/c++draft/lex.phases
  - source_id: cpp-draft-cpp-scope
    title: "C++ working draft: Scope of macro definitions ([cpp.scope])"
    url: https://eel.is/c++draft/cpp.scope
  - source_id: cpp-draft-dcl-constexpr
    title: "C++ working draft: The constexpr and consteval specifiers ([dcl.constexpr])"
    url: https://eel.is/c++draft/dcl.constexpr
  - source_id: cpp-draft-dcl-init-list
    title: "C++ working draft: List-initialization ([dcl.init.list])"
    url: https://eel.is/c++draft/dcl.init.list
---

## Question code

```cpp
constexpr int MAX_SENSORS = 16;
// vs  #define MAX_SENSORS 16
```

## Short answer

**It has type and scope – type-safe, unlike textual substitution.**

A `constexpr` variable has a type and ordinary scope, and its initializer must be a constant expression.[^iso-cpp-n4861][^cpp-draft-dcl-constexpr] A `#define` is preprocessor text substitution: the macro has no type and no scope, and the replacement happens in translation phase 4.[^cpp-draft-cpp-replace][^cpp-draft-lex-phases][^cpp-draft-cpp-scope]

Rule: integer compile-time constants in C++ are `constexpr`, not `#define`; `#define` stays for conditional compilation.

## Detailed explanation

TODO
