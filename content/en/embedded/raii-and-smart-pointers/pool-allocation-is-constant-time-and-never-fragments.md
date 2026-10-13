---
id: emb-raii-0017
title: "What is arena or pool allocation in the context of RAII?"
description: "Allocation of fixed-size blocks from an array: no external fragmentation between blocks, controlled lifetime."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-13; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: zephyr-memory-slabs
    title: "Zephyr Project documentation: Memory Slabs"
    url: https://docs.zephyrproject.org/latest/kernel/memory_management/slabs.html
    accessed: 2026-10-13
    kind: official
    version: "latest"
    applicability: "States that slab blocks all have one fixed size with no wasted space between them, which avoids fragmentation concerns, and that unallocated blocks are tracked with a linked list. Gives no allocation time bound and does not describe other pools."
  - source_id: cpp-draft-basic-life
    title: "C++ working draft: Object lifetime ([basic.life])"
    url: https://eel.is/c++draft/basic.life
    accessed: 2026-10-13
    kind: spec
    version: "working draft"
    applicability: "Paragraph 6: a program may end the lifetime of a class-type object without invoking its destructor by reusing the storage; the destructor is then not implicitly invoked, and correct behavior often depends on it being invoked. Does not describe arenas or pools."
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
    accessed: 2026-10-13
    kind: spec
    version: "working draft"
    applicability: "Paragraph 2, note 1: on exit from a scope in any way, automatic objects constructed in it are destroyed in reverse order of construction; with std::exit or std::abort their destruction may not happen. Does not describe pools or arenas."
---

## Short answer

**Allocation from fixed-size blocks: no external fragmentation between blocks, with a controlled lifetime.**

A Zephyr memory slab keeps free blocks in a linked list.[^zephyr-memory-slabs] From that structure, allocation takes the first block, with time independent of the block count; a looping search has no such guarantee.

Trivial objects can simply be dropped by an arena reset; non-trivial destructors must be called before it, since storage reuse does not invoke them.[^cpp-draft-basic-life]

Rule: no external fragmentation, but not zero cost: every object occupies a whole block.[^zephyr-memory-slabs]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
