---
id: emb-tmplcx-0005
title: "What is a constexpr function?"
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
    title: "C++ working draft: The constexpr specifier ([dcl.constexpr])"
    url: https://eel.is/c++draft/dcl.constexpr
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
---

## Short answer

**A function that can be called in a constant expression; in such a context it is evaluated at compile time, elsewhere it is an ordinary call.**

A call to a constexpr function gives the same result as a call to an equivalent non-constexpr function, but it can appear in a constant expression.[^cpp-draft-dcl-constexpr] A constexpr variable must be constant-initializable, so it needs no dynamic initialization at startup.[^cpp-draft-basic-start-static]

Rule: `constexpr` does not guarantee compile-time evaluation of every call; a constant context, such as `static_assert`, is required.

## Detailed explanation

TODO
