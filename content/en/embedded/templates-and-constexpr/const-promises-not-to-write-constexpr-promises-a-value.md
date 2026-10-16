---
id: emb-tmplcx-0007
title: "What is the difference between `const` and `constexpr`?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-dcl-constexpr
    title: "C++ working draft: The constexpr and consteval specifiers ([dcl.constexpr])"
    url: https://eel.is/c++draft/dcl.constexpr
  - source_id: cpp-draft-expr-const
    title: "C++ working draft: Constant expressions ([expr.const])"
    url: https://eel.is/c++draft/expr.const
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
  - source_id: cpp-draft-basic-start-dynamic
    title: "C++ working draft: Dynamic initialization of non-block variables ([basic.start.dynamic])"
    url: https://eel.is/c++draft/basic.start.dynamic
---

## Short answer

**`const` means "I will not modify it", but the value may be computed at runtime. `constexpr` means "can be a constant expression".**

For embedded, `constexpr` is stronger: an initializer that is not a constant expression is a compile error.[^cpp-draft-dcl-constexpr] A `constexpr` variable with static storage is initialized statically, with no dynamic initialization at startup.[^cpp-draft-expr-const][^cpp-draft-basic-start-static]

Rule: for compile-time constants and tables use `constexpr`, not just `const`.

## Detailed explanation

TODO
