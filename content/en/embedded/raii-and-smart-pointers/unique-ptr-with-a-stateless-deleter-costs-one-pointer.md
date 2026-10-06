---
id: emb-raii-0008
title: "What overhead does `unique_ptr` have compared with a raw pointer?"
description: "With a stateless deleter, `unique_ptr` usually has the size of one raw pointer, with no control block and no reference counting; an optimizing compiler usually inlines the teardown call."
track: embedded
section: raii-and-smart-pointers
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
  - source_id: cpp-draft-unique-ptr-general
    title: "C++ working draft: Unique-ownership pointers, General ([unique.ptr.general])"
    url: https://eel.is/c++draft/unique.ptr.general
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines a unique pointer as an object that stores a pointer and disposes of it through an associated deleter when itself destroyed, with strict ownership; unique_ptr is not copyable but is movable. Says nothing about the size of unique_ptr."
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines the unique_ptr destructor (`if (get()) get_deleter()(get());`) and that unique_ptr stores a pointer and a deleter. Does not govern the size of unique_ptr or inlining."
  - source_id: cpp-draft-lambda-closure
    title: "C++ working draft: Closure types ([expr.prim.lambda.closure])"
    url: https://eel.is/c++draft/expr.prim.lambda.closure
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Says the closure type is not an aggregate and is not final, and that an implementation may define it differently, including its size and alignment. So the standard does not fix the size of a closure type."
  - source_id: cpp-draft-lambda-capture
    title: "C++ working draft: Lambda captures ([expr.prim.lambda.capture])"
    url: https://eel.is/c++draft/expr.prim.lambda.capture
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Says an unnamed non-static data member is declared in the closure type for each entity captured by copy, while for entities captured by reference this is unspecified. Does not define sizeof of the closure type or of unique_ptr."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Section 3.1.2.3: a class parameter that is non-trivial for the purposes of calls (including one with a non-trivial destructor) is passed by the caller by reference to a temporary, and the caller calls its destructor after the call, rather than by the base C ABI rules, for example in a register. This is the ABI GCC uses on x86-64; for other platforms, including Arm, check the toolchain's own ABI."
  - source_id: cppcg-r21-prefer-unique-ptr
    title: "C++ Core Guidelines: R.21 – Prefer unique_ptr over shared_ptr unless you need to share ownership"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r21-prefer-unique_ptr-over-shared_ptr-unless-you-need-to-share-ownership
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "A guideline: unique_ptr is simpler, more predictable and faster because it keeps no use count. It is a recommendation, not a language requirement, and does not apply when ownership is truly shared."
  - source_id: cppcg-f7-smart-pointer-params
    title: "C++ Core Guidelines: F.7 – For general use, take T* or T& arguments rather than smart pointers"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#f7-for-general-use-take-t-or-t-arguments-rather-than-smart-pointers
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "A guideline: a function that does not manage lifetime should take `T*` or `T&`, and a smart pointer parameter means transferring or sharing ownership. Does not discuss the ABI cost of passing `unique_ptr` by value."
---

## Short answer

**With a stateless deleter, `unique_ptr` usually has the size of one raw pointer, but the standard does not guarantee it.** `unique_ptr` has strict ownership and is not copyable, so it needs neither a control block nor reference counting.[^cpp-draft-unique-ptr-general] The deleter type is known at compile time, so an optimizing compiler usually inlines the teardown call. If the deleter has state or is a function pointer, `sizeof(unique_ptr)` usually grows. Rule: `unique_ptr` is the usual choice for a single owner; keep its deleter stateless.[^cppcg-r21-prefer-unique-ptr]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
