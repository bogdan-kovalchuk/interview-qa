---
id: emb-cppoop-0009
title: "Trap: why can merely declaring a destructor inflate ROM?"
description: "A non-trivial destructor on a global object forces its destruction to be registered (__cxa_atexit or __aeabi_atexit) and may pull in the atexit runtime, wasting ROM bytes."
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
  - source_id: itanium-abi-atexit
    title: "Itanium C++ ABI: DSO Object Destruction API"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#dso-dtor-runtime-api
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Section 3.3.6.3 says that after constructing a global (or local static) object that will require destruction on exit, a termination function is registered through __cxa_atexit. This is an ABI, not the language standard; it does not give any runtime size."
  - source_id: arm-cpp-abi
    title: "C++ ABI for the Arm Architecture (CPPABI32)"
    url: https://raw.githubusercontent.com/ARM-software/abi-aa/main/cppabi32/cppabi32.rst
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "In the Static object destruction section: the Arm ABI requires static object destruction to be registered through __aeabi_atexit instead of __cxa_atexit; the list of destructions may be allocated statically, with a maximum length equal to the number of __aeabi_atexit call sites. This is the Arm ABI; it does not give any runtime code size."
  - source_id: cpp-draft-basic-start-term
    title: "C++ working draft: Termination ([basic.start.term])"
    url: https://eel.is/c++draft/basic.start.term
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "States that constructed objects with static storage duration are destroyed as part of a call to std::exit, that returning from main invokes std::exit, and that std::abort runs no destructors. Does not say whether main returns in firmware."
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "Defines a trivial destructor: not user-provided, not virtual, and the destructors of all direct bases and class-type members are trivial too. Does not say whether the compiler registers an object's destruction."
  - source_id: cpp-draft-basic-life
    title: "C++ working draft: Object lifetime ([basic.life])"
    url: https://eel.is/c++draft/basic.life
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "States that a program may end the lifetime of a class-type object without calling its destructor (by reusing or releasing its storage), and that program correctness often depends on the destructor being called."
  - source_id: gcc-cxx-cxa-atexit
    title: "GCC: C++ Dialect Options, -fuse-cxa-atexit"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html#index-fuse-cxa-atexit
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "States that -fuse-cxa-atexit registers destructors of objects with static storage duration through __cxa_atexit rather than atexit, is required for fully standards-compliant handling of static destructors, and works only if the C library supports __cxa_atexit. Says nothing about code size."
  - source_id: gcc-int-init-macros
    title: "GCC Internals: Macros Controlling Initialization Routines"
    url: https://gcc.gnu.org/onlinedocs/gccint/Macros-for-Initialization.html
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "Describes the target hook TARGET_DTORS_FROM_CXA_ATEXIT: destructors are either queued to run from __cxa_atexit or handled by the target's native ctors/dtors collection. Does not say which variant a given target and libc use."
---

## Short answer

<span class="warn">A global object with a non-trivial destructor makes the compiler register its destruction at startup (`__cxa_atexit`, `__aeabi_atexit` on Arm), which can pull in the atexit runtime – extra ROM.</span>[^itanium-abi-atexit][^arm-cpp-abi] The destructor runs only on `exit` or when `main` returns,[^cpp-draft-basic-start-term] and in firmware `main()` normally never returns, so this infrastructure is dead weight. The `-fno-use-cxa-atexit` flag only changes the mechanism, so its effect depends on the target.[^gcc-cxx-cxa-atexit]

Protection: make the destructor trivial (`= default`, no `virtual`)[^cpp-draft-class-dtor] or create the object in static storage with placement new and never destroy it.

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
