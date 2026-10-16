---
id: emb-raii-0003
title: "What does an RAII lock guard for an RTOS mutex look like?"
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
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
  - source_id: cpp-draft-basic-stc-auto
    title: "C++ working draft: Automatic storage duration ([basic.stc.auto])"
    url: https://eel.is/c++draft/basic.stc.auto
  - source_id: cpp-draft-except-ctor
    title: "C++ working draft: Stack unwinding ([except.ctor])"
    url: https://eel.is/c++draft/except.ctor
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
  - source_id: cppcg-cp20
    title: "C++ Core Guidelines: CP.20 – Use RAII, never plain lock()/unlock()"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp20-use-raii-never-plain-lockunlock
  - source_id: cppcg-cp44
    title: "C++ Core Guidelines: CP.44 – Remember to name your lock_guards and unique_locks"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp44-remember-to-name-your-lock_guards-and-unique_locks
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
