---
id: emb-raii-0019
title: "How does RAII solve the early-return problem between lock and unlock?"
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
  - source_id: cppcg-cp20
    title: "C++ Core Guidelines: CP.20 – Use RAII, never plain lock()/unlock()"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp20-use-raii-never-plain-lockunlock
  - source_id: cppcg-cp44
    title: "C++ Core Guidelines: CP.44 – Remember to name your lock_guards and unique_locks"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp44-remember-to-name-your-lock_guards-and-unique_locks
  - source_id: cpp-draft-except-ctor
    title: "C++ working draft: Stack unwinding ([except.ctor])"
    url: https://eel.is/c++draft/except.ctor
  - source_id: cpp-draft-csetjmp-syn
    title: "C++ working draft: C library setjmp/longjmp header ([csetjmp.syn])"
    url: https://eel.is/c++draft/csetjmp.syn
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
