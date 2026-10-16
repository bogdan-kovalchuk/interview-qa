---
id: emb-tmplcx-0001
title: "What is a function template and why is it better than a macro?"
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
  - source_id: cpp-draft-expr-call
    title: "C++ working draft: Function call ([expr.call])"
    url: https://eel.is/c++draft/expr.call
  - source_id: cpp-draft-temp-deduct-call
    title: "C++ working draft: Deducing template arguments from a function call ([temp.deduct.call])"
    url: https://eel.is/c++draft/temp.deduct.call
---

## Question code

```cpp
template<typename T>
T clamp(T v, T lo, T hi) {
  return v < lo ? lo : (v > hi ? hi : v);
}
```

## Short answer

**One definition that works for any type that supports the operations its body uses, with full type checking.**

Unlike a macro, which only substitutes argument text,[^cpp-draft-cpp-replace] a function template evaluates each argument exactly once, without double evaluation.[^cpp-draft-expr-call] If the arguments give different deduced types for T, the call is rejected.[^cpp-draft-temp-deduct-call]

Rule: a function template is usually the better choice over a function-like macro, but macros remain necessary for stringizing (`#`) and token pasting (`##`).[^cpp-draft-cpp-replace][^embeddedinterviewlab]

## Detailed explanation

TODO
