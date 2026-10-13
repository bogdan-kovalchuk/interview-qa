---
id: emb-raii-0016
title: "What is a static RAII singleton and when do its constructor and destructor run?"
description: "Function-local static: the constructor runs on the first pass through its declaration; the destructor runs at exit, not at abort."
track: embedded
section: raii-and-smart-pointers
level: junior
type: mechanism
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
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
    accessed: 2026-10-13
    kind: spec
    version: "working draft"
    applicability: "Paragraph 3: dynamic initialization of a block variable with static storage duration happens the first time control passes through its declaration; after an exception from the constructor it is retried, and a concurrent entry waits for completion. Does not describe the compiler's thread-safe code."
  - source_id: cpp-draft-basic-start-term
    title: "C++ working draft: Termination ([basic.start.term])"
    url: https://eel.is/c++draft/basic.start.term
    accessed: 2026-10-13
    kind: spec
    version: "working draft"
    applicability: "Paragraph 1: constructed objects with static storage duration are destroyed as part of a call to std::exit, and returning from main invokes std::exit. Does not say whether main returns in firmware."
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraphs 3 and 5: _Exit and std::abort terminate the program without executing destructors for objects with static storage duration. Does not describe behavior after a hardware reset."
  - source_id: gcc-cxx-threadsafe-statics
    title: "GCC: C++ Dialect Options, -fno-threadsafe-statics"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html#index-fthreadsafe-statics
    accessed: 2026-10-13
    kind: official
    version: "current"
    applicability: "States that -fno-threadsafe-statics removes the extra code for thread-safe initialization of local statics under the C++ ABI, slightly reducing code size where thread safety is not needed. Gives no exact byte saving."
---

## Question code

```c
Driver& instance() {
  static Driver d; // ctor - при 1-му виклику
  return d;
}
```

## Short answer

**Function-local static: the constructor runs once, on the first pass through its declaration; the destructor runs at exit, including return from main.**[^cpp-draft-basic-start-term]

The object is created on the first pass through the declaration, not at program start, so this is lazy initialization that avoids the static initialization order fiasco between translation units.[^cpp-draft-stmt-dcl] But GCC adds thread-safe initialization code by default; `-fno-threadsafe-statics` removes it, leaving a concurrent first entry unsynchronized.[^gcc-cxx-threadsafe-statics]

Rule: Meyers' singleton is heap-free but not always runtime-free; check the generated code on your toolchain.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
