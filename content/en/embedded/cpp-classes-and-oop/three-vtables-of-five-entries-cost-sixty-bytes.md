---
id: emb-cppoop-0014
title: "Estimate the simplified cost: 3 classes with 5 virtual methods each. How much ROM for the vtables?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
---

## Short answer

**Estimate for the function-pointer entries only: 60 bytes of ROM**: 3 vtables × 5 entries × 4 bytes on a 32-bit target. A real Itanium-style vtable has two more slots (offset-to-top, typeinfo pointer), giving 3 × (5 + 2) × 4 = 84 bytes, and a virtual destructor adds another slot.[^itanium-cxx-abi] In RAM, each object adds a vptr: 100 objects × 4 bytes = 400 bytes. Count vtables per class and vptrs per instance; on a small MCU many objects make the vptr cost noticeable.

## Detailed explanation

TODO
