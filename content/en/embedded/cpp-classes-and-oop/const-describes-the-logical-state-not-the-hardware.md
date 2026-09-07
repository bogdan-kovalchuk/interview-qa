---
id: emb-cppoop-0005
title: "Why are hardware access methods often marked `const` even though they change a register?"
description: "const refers to the logical state of the object, not the hardware; writing through an immutable pointer does not violate const."
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

**`const` refers to the logical state of the object, not the hardware.**

The `set()` method does not change the fields of the `Gpio` object (the pointer and pin are immutable) – it writes to a hardware register through them. So the object is logically `const`, and the method can be marked as such.

Rule: a const member is valid if it does not modify the object's members; a hardware side effect does not contradict this.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
