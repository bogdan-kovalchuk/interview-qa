---
id: emb-raii-0020
title: "How is RAII better than manual init/deinit?"
description: "RAII guarantees the destructor runs on scope exit, safe early return, one destructor instead of repetition, and automatic destruction order."
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
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
    accessed: 2026-10-13
    kind: spec
    version: "working draft"
    applicability: "Paragraph 2, note 1: on exit from a scope in any way, automatic objects are destroyed in reverse order of construction; with std::exit or std::abort they may not be destroyed. Does not compare with manual code or describe runtime cost."
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "States that std::exit does not destroy automatic objects, and that std::abort and _Exit terminate the program without executing destructors for automatic and static objects. Does not describe inlining."
  - source_id: cppcg-cp20
    title: "C++ Core Guidelines: CP.20 – Use RAII, never plain lock()/unlock()"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp20-use-raii-never-plain-lockunlock
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Guideline: use an RAII wrapper instead of manual lock() and unlock(), because unlock() is easy to forget, skip with a return, or skip with an exception. Says nothing about interrupts or bare metal."
---

## Short answer

- **Cleanup guarantee:** on scope exit the compiler calls the destructor; by hand the programmer must remember;
- **Error path:** early return is safe vs every exit is a chance for a bug;
- **Duplication:** the dtor is written once vs repeated at every exit;
- **Order:** automatic reverse destruction vs manual calls the programmer must write;
- **Runtime:** with GCC `-O2`, usually the same unlock call as manual code; an empty dtor emits nothing, but check the asm.

Rule: RAII adds no new capabilities; it removes forgotten-cleanup errors on scope exit.[^cpp-draft-stmt-jump]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
