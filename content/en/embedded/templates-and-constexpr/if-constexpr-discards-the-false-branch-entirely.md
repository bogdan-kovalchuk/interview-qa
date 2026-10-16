---
id: emb-tmplcx-0018
title: "How does `if constexpr` work and why is it better than `#ifdef`?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-stmt-if
    title: "C++ working draft: The if statement ([stmt.if])"
    url: https://eel.is/c++draft/stmt.if
  - source_id: cpp-draft-cpp-cond
    title: "C++ working draft: Conditional inclusion ([cpp.cond])"
    url: https://eel.is/c++draft/cpp.cond
  - source_id: cpp-draft-temp-res
    title: "C++ working draft: Name resolution ([temp.res])"
    url: https://eel.is/c++draft/temp.res
---

## Question code

```cpp
template<typename P>
void init_uart() {
  if constexpr (std::is_same_v<P, STM32F4>) {
    USART1->BRR = compute_brr(115200);
  } else {
    static_assert(always_false<P>, "unsupported");
  }
}
```

## Short answer

**The condition is evaluated at compile time; in a template the discarded branch is not instantiated, so no code is generated for it.**[^cpp-draft-stmt-if] The preprocessor `#ifdef` skips the tokens of the unselected branch.[^cpp-draft-cpp-cond] The compiler, however, checks the syntax of a discarded `if constexpr` branch.[^cpp-draft-stmt-if] Parts of the discarded branch that depend on a template parameter are not instantiated, so their type errors do not appear.[^cpp-draft-stmt-if] Rule: `if constexpr` is a type-safe replacement for `#ifdef` in platform-dependent code.

## Detailed explanation

TODO
