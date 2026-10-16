---
id: emb-raii-0004
title: "Trap: why must a lock guard forbid copying (`= delete`)?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cmsis-rtos2-mutex
    title: "CMSIS-RTOS2: Mutex Management"
    url: https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__MutexMgmt.html
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: Copy/move constructors ([class.copy.ctor])"
    url: https://eel.is/c++draft/class.copy.ctor
  - source_id: cpp-draft-class-copy-assign
    title: "C++ working draft: Copy/move assignment operator ([class.copy.assign])"
    url: https://eel.is/c++draft/class.copy.assign
  - source_id: cpp-draft-dcl-fct-def-delete
    title: "C++ working draft: Deleted definitions ([dcl.fct.def.delete])"
    url: https://eel.is/c++draft/dcl.fct.def.delete
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
