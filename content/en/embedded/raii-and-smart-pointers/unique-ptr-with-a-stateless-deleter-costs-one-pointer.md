---
id: emb-raii-0008
title: "What overhead does `unique_ptr` have compared with a raw pointer?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-unique-ptr-general
    title: "C++ working draft: Unique-ownership pointers, General ([unique.ptr.general])"
    url: https://eel.is/c++draft/unique.ptr.general
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
  - source_id: cpp-draft-lambda-closure
    title: "C++ working draft: Closure types ([expr.prim.lambda.closure])"
    url: https://eel.is/c++draft/expr.prim.lambda.closure
  - source_id: cpp-draft-lambda-capture
    title: "C++ working draft: Lambda captures ([expr.prim.lambda.capture])"
    url: https://eel.is/c++draft/expr.prim.lambda.capture
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: cppcg-r21-prefer-unique-ptr
    title: "C++ Core Guidelines: R.21 – Prefer unique_ptr over shared_ptr unless you need to share ownership"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r21-prefer-unique_ptr-over-shared_ptr-unless-you-need-to-share-ownership
  - source_id: cppcg-f7-smart-pointer-params
    title: "C++ Core Guidelines: F.7 – For general use, take T* or T& arguments rather than smart pointers"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#f7-for-general-use-take-t-or-t-arguments-rather-than-smart-pointers
---

## Short answer

**With a stateless deleter, `unique_ptr` usually has the size of one raw pointer, but the standard does not guarantee it.** `unique_ptr` has strict ownership and is not copyable, so it needs neither a control block nor reference counting.[^cpp-draft-unique-ptr-general] The deleter type is known at compile time, so an optimizing compiler usually inlines the teardown call. If the deleter has state or is a function pointer, `sizeof(unique_ptr)` usually grows. Rule: `unique_ptr` is the usual choice for a single owner; keep its deleter stateless.[^cppcg-r21-prefer-unique-ptr]

## Detailed explanation

TODO
