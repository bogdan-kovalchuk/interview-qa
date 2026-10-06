---
id: emb-cppoop-0013
title: "What does a virtual function cost in memory?"
description: "One vtable per polymorphic class in ROM and one hidden vptr per polymorphic object in RAM"
track: embedded
section: cpp-classes-and-oop
level: junior
type: concept
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
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines a virtual function and a polymorphic class and notes that virtual functions support dynamic binding; this clause does not mention a vtable or vptr, so they are an implementation detail."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Sections 2.4 and 2.5 describe the vptr of a dynamic class (at offset 0 when there is no primary base), the vtable as a table for dispatch, virtual base access and RTTI, one set of tables per most-derived class, the offset-to-top and typeinfo pointer slots, and the pair of entries for a virtual destructor. This is an ABI, not the language standard; it says nothing about which memory section holds a vtable."
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Names the generic (Itanium) C++ ABI as the base standard for Arm; its summary of differences does not mention the vtable layout (section 2.5), so it declares no Arm deviation there. It does not say where the linker places a vtable."
---

## Short answer

**Typically one vtable per polymorphic class in ROM (`.rodata`) and one hidden vptr per polymorphic object in RAM.** Rough estimate: vtable ≈ number of virtual functions × pointer size plus ABI slots (offset-to-top, typeinfo), with a virtual destructor taking two entries; vptr ≈ one pointer per instance, more with several polymorphic bases.[^itanium-cxx-abi] These are ABI details, not C++ standard rules; Arm declares no different ones.[^arm-cpp-abi] With hundreds of objects the RAM cost becomes significant.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
