---
id: emb-cppoop-0029
title: "How does a static member function differ from an ordinary one?"
description: "A static member function has no this pointer and is not bound to an instance, making it useful as a C callback thunk"
track: embedded
section: cpp-classes-and-oop
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

## Short answer

**A static member function has no `this`** – it is not bound to an instance.

Therefore it can be called as `Class::func()` and cannot access non-static members. In practice it is often used as a callback thunk for a C API (application programming interface), because its type resembles an ordinary function pointer; for strict C linkage a separate `extern "C"` wrapper function is sometimes needed.

Rule: a static member function is a convenient bridge between a C++ class and a C API, but check the signature and linkage requirements of the particular callback API.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
