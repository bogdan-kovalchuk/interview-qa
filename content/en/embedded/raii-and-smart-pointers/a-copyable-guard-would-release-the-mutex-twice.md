---
id: emb-raii-0004
title: "Trap: why must a lock guard `= delete` its copy and move operations?"
description: "Copying a lock guard would cause two destructors to release the same mutex, so copy and move must be deleted to guarantee exactly one owner and one release."
track: embedded
section: raii-and-smart-pointers
level: junior
type: pitfall
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
LockGuard(const LockGuard&) = delete;
LockGuard& operator=(const LockGuard&) = delete;
```

## Short answer

<span class="warn">If the guard could be copied, two destructors would release the same mutex – double-release and instant corruption.</span>

Banning copying guarantees exactly one lock owner and exactly one release.

Protection: any resource wrapper class must be non-copyable (`= delete`) or move-only.[^embeddedinterviewlab]

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
