---
id: emb-raii-0021
title: "Why are nested resources released in reverse order automatically?"
description: "Destructors of local objects are called in reverse order of construction."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-13; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements ([stmt.jump])"
    url: https://eel.is/c++draft/stmt.jump
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Note: on exit from a scope, however accomplished, automatic-storage objects constructed in that scope are destroyed in reverse order of construction. Says nothing about exit(), abort() or longjmp."
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says that bases and non-static members are destroyed in reverse order of the completion of their constructors. Does not discuss local variables."
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says that std::abort ends the program without running destructors for objects of automatic, thread or static storage duration; a footnote says exit() does not destroy automatic objects. Says nothing about embedded runtimes."
  - source_id: cpp-draft-support-runtime
    title: "C++ working draft: Other runtime support ([support.runtime])"
    url: https://eel.is/c++draft/support.runtime
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says a setjmp/longjmp pair has undefined behavior if replacing it with catch and throw would invoke non-trivial destructors of automatic objects. Does not describe any particular MCU runtime."
---

## Short answer

**Destructors of local objects are called in reverse order of construction.**

If you acquired clock, then SPI, then CS, the release order will be CS -> SPI -> clock, which is usually the correct teardown order.[^cpp-draft-stmt-jump] By hand, this is easy to mix up.

Rule: declare RAII guards in dependency order; reverse destruction happens when leaving a scope, but not on `exit()` or `abort()`, which do not destroy automatic objects.[^cpp-draft-support-start-term]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
