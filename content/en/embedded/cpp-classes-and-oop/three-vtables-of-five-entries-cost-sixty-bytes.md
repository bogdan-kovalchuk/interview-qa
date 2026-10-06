---
id: emb-cppoop-0014
title: "Estimate the simplified cost: 3 classes with 5 virtual methods each. How much ROM for the vtables?"
description: "Entries alone give 60 bytes of ROM (3 vtables × 5 entries × 4 bytes on 32-bit); a real vtable is larger because of ABI slots, and vptrs add RAM per object"
track: embedded
section: cpp-classes-and-oop
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Sections 2.4 and 2.5 describe a vtable as a sequence of offsets and function pointers with pointer size and alignment, the mandatory offset-to-top and typeinfo pointer slots, one entry per virtual function, a pair of entries for a virtual destructor, and the vptr at offset 0 of a dynamic class without a primary base. This is an ABI, not the language standard; the platform decides the actual pointer size."
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Names the generic (Itanium) C++ ABI as the base standard for Arm; its summary of differences does not mention the vtable layout (section 2.5), so it declares no Arm deviation there. It does not say where the linker places a vtable."
---

## Short answer

**Estimate for the function-pointer entries only: 60 bytes of ROM**: 3 vtables × 5 entries × 4 bytes on a 32-bit target. A real Itanium-style vtable has two more slots (offset-to-top, typeinfo pointer), giving 3 × (5 + 2) × 4 = 84 bytes, and a virtual destructor adds another slot.[^itanium-cxx-abi] In RAM, each object adds a vptr: 100 objects × 4 bytes = 400 bytes. Count vtables per class and vptrs per instance; on a small MCU many objects make the vptr cost noticeable.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
