---
id: emb-cppoop-0026
title: "Trap: you see a null vptr in a global object. What is the cause?"
description: "Most often global constructors have not run because startup did not walk the init array"
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
    applicability: "In the Top-level static object construction section: each translation unit contributes a fragment of the constructor vector in the .init_array section (SHT_INIT_ARRAY); each element is the address of a void(void) function that constructs that translation unit's global objects; run-time support code walks the vector in increasing address order; the ABI does not order translation units. This is the Arm ABI; other architectures and toolchains can differ."
  - source_id: cpp-draft-basic-start-static
    title: "C++ working draft: Static initialization ([basic.start.static])"
    url: https://eel.is/c++draft/basic.start.static
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "States that a variable with static storage duration is either constant-initialized or zero-initialized, and that all static initialization strongly happens before any dynamic initialization. Says nothing about the vptr, sections or startup."
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
---

## Short answer

<span class="warn">The most common cause is that startup did not run the constructors of global objects listed in `.init_array`.</span>[^arm-cpp-abi] An object that needs dynamic initialization is otherwise only zero-initialized, and the vptr of a polymorphic object is normally set by its constructor,[^cpp-draft-basic-start-static][^itanium-abi-ctor-vptr] so the first virtual call goes through a null vptr – undefined behavior, in practice usually a fault. Protection: make sure startup walks `.init_array` before `main()`; a null vptr also appears when an object is used before its constructor has run.

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
