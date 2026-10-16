---
id: emb-raii-0021
title: "Why are nested resources released in reverse order automatically?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements ([stmt.jump])"
    url: https://eel.is/c++draft/stmt.jump
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
  - source_id: cpp-draft-support-runtime
    title: "C++ working draft: Other runtime support ([support.runtime])"
    url: https://eel.is/c++draft/support.runtime
---

## Short answer

**Destructors of local objects are called in reverse order of construction.**

If you acquired clock, then SPI, then CS, the release order will be CS -> SPI -> clock, which is usually the correct teardown order.[^cpp-draft-stmt-jump] By hand, this is easy to mix up.

Rule: declare RAII guards in dependency order; reverse destruction happens when leaving a scope, but not on `exit()` or `abort()`, which do not destroy automatic objects.[^cpp-draft-support-start-term]

## Detailed explanation

TODO
