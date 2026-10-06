---
id: emb-raii-0004
title: "Trap: why must a lock guard forbid copying (`= delete`)?"
description: "Copying a lock guard would give one mutex two owners and two `osMutexRelease` calls: the first destructor drops the lock while the other copy still believes it holds it."
track: embedded
section: raii-and-smart-pointers
level: junior
type: pitfall
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
    applicability: "Describes the CMSIS-RTOS2 mutex API: osMutexRelease returns osErrorResource if the mutex was not acquired or the thread is not the owner; a recursive mutex (osMutexRecursive) must be released as many times as it was acquired. A specific RTOS implementation can behave differently outside the specification."
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: Copy/move constructors ([class.copy.ctor])"
    url: https://eel.is/c++draft/class.copy.ctor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that without a user-declared copy constructor one is implicitly declared (deprecated for a class with a user-declared destructor), that an implicit move constructor is declared only if, among other conditions, there is no user-declared copy constructor and no user-declared destructor, and that an implicitly defined move constructor performs a memberwise move. Does not cover optimizations."
  - source_id: cpp-draft-class-copy-assign
    title: "C++ working draft: Copy/move assignment operator ([class.copy.assign])"
    url: https://eel.is/c++draft/class.copy.assign
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraph 2: if the class has no user-declared copy assignment operator, one is implicitly declared; so deleting only the copy constructor does not forbid assignment. The deprecation details for this operator are not covered."
  - source_id: cpp-draft-dcl-fct-def-delete
    title: "C++ working draft: Deleted definitions ([dcl.fct.def.delete])"
    url: https://eel.is/c++draft/dcl.fct.def.delete
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraph 2: a construct that designates a deleted function (a call, a pointer to it) is ill-formed; example 3 shows a move-only class with deleted copy constructor and copy assignment and defaulted move operations. Says nothing about RTOS behavior."
---

## Question code

```c
LockGuard(const LockGuard&) = delete;
LockGuard& operator=(const LockGuard&) = delete;
```

## Short answer

<span class="warn">Copying the guard would give one mutex two owners and two `osMutexRelease` calls.</span>

The first destructor drops the lock while the code in the other copy's scope still thinks the mutex is held; the second call returns `osErrorResource` in CMSIS-RTOS2 if the mutex was not acquired or the thread is not the owner.[^cmsis-rtos2-mutex] The compiler still generates a copy constructor for a class with a user-declared destructor (deprecated),[^cpp-draft-class-copy-ctor] so copying must be forbidden explicitly.

Protection: a resource wrapper class must be non-copyable (`= delete` on copy) or move-only.[^cpp-draft-dcl-fct-def-delete]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
