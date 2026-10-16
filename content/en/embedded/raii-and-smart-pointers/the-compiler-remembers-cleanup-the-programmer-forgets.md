---
id: emb-raii-0020
title: "How is RAII better than manual init/deinit?"
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
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
  - source_id: cppcg-cp20
    title: "C++ Core Guidelines: CP.20 – Use RAII, never plain lock()/unlock()"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp20-use-raii-never-plain-lockunlock
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
