---
id: emb-cppoop-0015
title: "What is the vptr and where is it stored?"
description: "A hidden pointer inside every object with virtual functions, pointing at the vtable of its dynamic type"
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

**A vptr is a hidden pointer inside every object with virtual functions, pointing at the vtable of its dynamic type.**

It is typically added by the compiler as a hidden member, so `sizeof` grows by roughly one pointer size (4 bytes on 32-bit). The exact vptr position is ABI-dependent, not part of the C++ standard.

Rule: the presence of even one virtual function typically adds a vptr to every instance.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
