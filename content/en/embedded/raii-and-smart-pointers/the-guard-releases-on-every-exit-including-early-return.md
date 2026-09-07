---
id: emb-raii-0019
title: "How does RAII solve the early-return problem between lock and unlock?"
description: "An RAII guard releases the mutex on every normal scope exit, including early return."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
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

```c
// C: баг на error-шляху
mutex_lock(&m);
if (error) return -1; // забули unlock!
mutex_unlock(&m);
```

## Short answer

**An RAII guard releases the mutex on every normal scope exit, including early return.**

```cpp
{ LockGuard lock(m);
  if (error) return -1; } // dtor розблокує
```

A typical failure mode: an early return between lock and unlock causes deadlock due to a forgotten unlock on the error path.

Rule: RAII turns discipline (remembering to unlock) into a structural guarantee.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
