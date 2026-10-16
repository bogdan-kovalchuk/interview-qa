---
id: emb-tmplcx-0019
title: "Trap: how is `if constexpr` safer than `#ifdef` against mistakes?"
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

## Short answer

<span class="warn">`#ifdef` skips the unselected branch without checking C++ syntax – typos in it are not visible until that branch is enabled.</span>[^cpp-draft-cpp-cond]

`if constexpr` makes the compiler check the syntax of both branches, so a syntax error in the "inactive" platform shows up immediately.[^cpp-draft-stmt-if]

However, type errors that depend on a template parameter do not show up in the discarded branch, because it is not instantiated.[^cpp-draft-stmt-if]

Defense: for platform switching prefer `if constexpr` and build every platform, because dependent parts are checked only on instantiation.

## Detailed explanation

TODO
