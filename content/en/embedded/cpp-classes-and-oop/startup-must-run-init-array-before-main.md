---
id: emb-cppoop-0008
title: "Trap: when do global constructors run and what must startup do?"
description: "Global constructors are run by walking .init_array; on bare metal startup code must do it before main()."
track: embedded
section: cpp-classes-and-oop
level: junior
type: pitfall
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
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "In the Top-level static object construction section: each translation unit contributes a fragment of the constructor vector in the .init_array section (SHT_INIT_ARRAY); each element is the address of a void(void) function that constructs that translation unit's global objects; run-time support code walks the vector in increasing address order; the ABI does not order translation units; elements may also be self-relative. This is the Arm ABI; other architectures and toolchains can differ."
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "States that a variable with static storage duration is either constant-initialized or zero-initialized, and that all static initialization strongly happens before any dynamic initialization. Does not say who calls dynamic initialization or when."
  - source_id: cpp-draft-basic-start-dynamic
    title: "C++ working draft: Dynamic initialization of non-block variables ([basic.start.dynamic])"
    url: https://eel.is/c++draft/basic.start.dynamic
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "States that it is implementation-defined whether dynamic initialization of a variable with static storage duration is sequenced before the first statement of main or deferred. Does not define the calling mechanism (sections, startup code)."
  - source_id: itanium-abi-ctor-vptr
    title: "Itanium C++ ABI: Virtual tables During Object Construction"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#vtable-ctor-general
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Section 2.6.1 says an object's vptr is normally set by the constructor of a class (to that class's vtable). This is an ABI, not the language standard; other ABIs can differ in detail."
  - source_id: gnu-ld-manual-sections
    title: "GNU ld manual: SECTIONS and input section description"
    url: https://sourceware.org/binutils/docs/ld.html
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "Describes the .init_array.NNNNN and .ctors.NNNNN sections (NNNNN relates to the GCC init_priority) and KEEP() for sections that must survive --gc-sections (examples: .init, .ctors). Does not say what any particular project's linker script contains."
  - source_id: gcc-int-initialization
    title: "GCC Internals: How Initialization Functions Are Handled"
    url: https://gcc.gnu.org/onlinedocs/gccint/Initialization.html
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "States that compiler-generated initialization functions must be called before main, and that the traditional GCC mechanisms are the .ctors/.dtors and .init sections, falling back to a __main call. Does not mention .init_array."
---

## Short answer

<span class="warn">Constructors of global objects that need dynamic initialization are run by functions listed in the `.init_array` section; run-time support code (on bare metal, your startup code) must walk that array before `main()`.</span>[^arm-cpp-abi] If it does not, such an object stays merely zero-initialized, and the vptr of a polymorphic object is normally set by its constructor.[^cpp-draft-basic-start-static][^itanium-abi-ctor-vptr] The standard itself leaves it implementation-defined whether this initialization happens before the first statement of `main()`.[^cpp-draft-basic-start-dynamic]

Protection: make sure startup iterates `.init_array` before `main()`; this is a common bug when porting C++ to bare metal.

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
