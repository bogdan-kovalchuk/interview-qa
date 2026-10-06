---
id: emb-raii-0003
title: "What does an RAII lock guard for an RTOS mutex look like?"
description: "The constructor acquires the RTOS mutex and the destructor releases it on scope exit, removing forgotten unlocks on error paths."
track: embedded
section: raii-and-smart-pointers
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cmsis-rtos2-mutex
    title: "CMSIS-RTOS2: Mutex Management"
    url: https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__MutexMgmt.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Describes the CMSIS-RTOS2 mutex API: osMutexAcquire and osMutexRelease (the calling thread blocks until the mutex is obtained, return codes, including osErrorResource when releasing a mutex that was not acquired or is not owned; not callable from an ISR), and the osMutexRecursive attribute. A specific RTOS implementation can behave differently outside the specification."
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraph 2: on every transfer of control within a function (including a return from it), automatic block variables active at the source point and not at the destination point are destroyed in reverse order of construction. Does not cover program termination through exit or abort and does not describe exceptions."
  - source_id: cpp-draft-basic-stc-auto
    title: "C++ working draft: Automatic storage duration ([basic.stc.auto])"
    url: https://eel.is/c++draft/basic.stc.auto
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraph 2: an automatic variable with initialization or a destructor with side effects cannot be destroyed before the end of its block or eliminated as an optimization, even if it looks unused (except copy/move elision). Does not apply to variables with a trivial destructor."
  - source_id: cpp-draft-except-ctor
    title: "C++ working draft: Stack unwinding ([except.ctor])"
    url: https://eel.is/c++draft/except.ctor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Describes destruction of automatic objects in reverse order when an exception is thrown, and that an exception from a constructor runs destructors for already initialized subobjects; does not apply when exceptions are disabled by the compiler."
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: wrap a resource with paired acquire/release in an object that acquires in the constructor and releases in the destructor; its examples are files, mutexes and memory, not hardware peripherals."
  - source_id: cppcg-cp20
    title: "C++ Core Guidelines: CP.20 – Use RAII, never plain lock()/unlock()"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp20-use-raii-never-plain-lockunlock
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline CP.20: take and release a lock through an RAII object rather than plain lock()/unlock(), because someone will forget the unlock, add a return or throw an exception. Its example is std::mutex, not an RTOS API."
  - source_id: cppcg-cp44
    title: "C++ Core Guidelines: CP.44 – Remember to name your lock_guards and unique_locks"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp44-remember-to-name-your-lock_guards-and-unique_locks
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline CP.44: an unnamed local object is a temporary that immediately goes out of scope, so the lock is not held to the end of the critical section. Its examples are std::lock_guard and std::unique_lock, not an RTOS guard."
---

## Question code

```cpp
class LockGuard {
  osMutexId_t m_;
public:
  explicit LockGuard(osMutexId_t m) : m_(m) {
    osMutexAcquire(m_, osWaitForever);
  }
  ~LockGuard() { osMutexRelease(m_); }
};
```

## Short answer

**The ctor acquires the mutex, the dtor releases it on scope exit.**

An RTOS is a real-time operating system. Every exit from the block (end, early `return`, `break`) runs the destructor and therefore `osMutexRelease`,[^cpp-draft-stmt-dcl] so no forgotten unlock is left on error paths;[^cppcg-cp20] with exceptions enabled the same happens during unwinding up to a handler.[^cpp-draft-except-ctor] The guard is usable only in thread context, and the `osMutexAcquire` status must be checked.[^cmsis-rtos2-mutex]

Rule: every acquire/release pair in a C API (application programming interface) is a lock guard candidate.[^cppcg-r1-raii]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
