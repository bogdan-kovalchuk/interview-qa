---
id: emb-raii-0019
title: "How does RAII solve the early-return problem between lock and unlock?"
description: "An RAII guard releases the mutex on every scope exit, including early return."
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
    applicability: "Paragraph 2, note 1: on exit from a scope in any way, automatic objects are destroyed in reverse order of construction; with std::exit or std::abort they may not be destroyed. Does not describe mutexes or RTOS behavior."
  - source_id: cppcg-cp20
    title: "C++ Core Guidelines: CP.20 – Use RAII, never plain lock()/unlock()"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp20-use-raii-never-plain-lockunlock
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Guideline: use an RAII wrapper instead of manual lock() and unlock(), because unlock() is easy to forget, skip with a return, or skip with an exception. Says nothing about interrupts or bare metal."
  - source_id: cppcg-cp44
    title: "C++ Core Guidelines: CP.44 – Remember to name your lock_guards and unique_locks"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp44-remember-to-name-your-lock_guards-and-unique_locks
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Guideline CP.44: an unnamed local object is a temporary that leaves scope immediately. In example (A), unique_lock<mutex>(m1) is a default-constructed local variable m1 that shadows the global m1 and locks nothing; (B), lock_guard<mutex> {m2}, locks and unlocks at once. Examples are std::lock_guard and std::unique_lock, not an RTOS guard."
  - source_id: cpp-draft-except-ctor
    title: "C++ working draft: Stack unwinding ([except.ctor])"
    url: https://eel.is/c++draft/except.ctor
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraphs 1–2: when an exception passes to a handler, automatic objects constructed after the try block was entered are destroyed (stack unwinding). Does not describe the case where exceptions are disabled by the compiler."
  - source_id: cpp-draft-csetjmp-syn
    title: "C++ working draft: C library setjmp/longjmp header ([csetjmp.syn])"
    url: https://eel.is/c++draft/csetjmp.syn
    accessed: 2026-10-13
    kind: spec
    version: "working draft"
    applicability: "Paragraph 2: a setjmp/longjmp pair has undefined behavior if replacing it with catch and throw would invoke non-trivial destructors of automatic objects. Does not describe exit or abort."
---

## Question code

```c
// C: баг на error-шляху
mutex_lock(&m);
if (error) return -1; // забули unlock!
mutex_unlock(&m);
```

## Short answer

**An RAII guard releases the mutex on every scope exit, including early return and an exception (if exceptions are enabled).**[^cpp-draft-stmt-jump][^cpp-draft-except-ctor] With exit, abort or longjmp this is not guaranteed: `longjmp` past an object with a non-trivial destructor is undefined behavior.[^cpp-draft-csetjmp-syn]

```cpp
{ LockGuard lock(m);
  if (error) return -1; } // dtor unlocks
```

A typical failure mode: an early return between lock and unlock can leave the mutex held, and the next attempt to take it may hang (deadlock).

Rule: RAII turns discipline (remembering to unlock) into a structural guarantee.[^cppcg-cp20]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
