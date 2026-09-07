---
id: emb-raii-0029
title: "Trap: what happens to the resource if a wrapper object is created on the heap and never deleted?"
description: "The destructor is never called so the resource is never freed, causing a leak despite being an RAII class."
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

## Short answer

<span class="warn">The destructor is never called -> the resource is never freed (leak), despite this being an RAII class.</span>

RAII guarantees cleanup only for objects with automatic (stack) lifetime or managed by a smart pointer. `new LockGuard(...)` without delete is the same forgotten unlock.

Defense: keep RAII objects on the stack or under `unique_ptr`, not as a bare `new`.[^embeddedinterviewlab]

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
