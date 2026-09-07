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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
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

An RTOS is a real-time operating system. Any normal exit from the block or an early `return` is guaranteed to call `osMutexRelease`; if exceptions are enabled, this also works during unwinding. That removes forgotten unlocks on error paths.

Rule: every acquire/release pair in a C API (application programming interface) is a lock guard candidate.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
