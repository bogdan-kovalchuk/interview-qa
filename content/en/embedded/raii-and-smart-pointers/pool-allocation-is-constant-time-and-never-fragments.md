---
id: emb-raii-0017
title: "What is arena or pool allocation in the context of RAII?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: zephyr-memory-slabs
    title: "Zephyr Project documentation: Memory Slabs"
    url: https://docs.zephyrproject.org/latest/kernel/memory_management/slabs.html
  - source_id: cpp-draft-basic-life
    title: "C++ working draft: Object lifetime ([basic.life])"
    url: https://eel.is/c++draft/basic.life
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
---

## Short answer

**Allocation from fixed-size blocks: no external fragmentation between blocks, with a controlled lifetime.**

A Zephyr memory slab keeps free blocks in a linked list.[^zephyr-memory-slabs] From that structure, allocation takes the first block, with time independent of the block count; a looping search has no such guarantee.

Trivial objects can simply be dropped by an arena reset; non-trivial destructors must be called before it, since storage reuse does not invoke them.[^cpp-draft-basic-life]

Rule: no external fragmentation, but not zero cost: every object occupies a whole block.[^zephyr-memory-slabs]

## Detailed explanation

TODO
