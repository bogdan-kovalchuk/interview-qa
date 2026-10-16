---
id: emb-raii-0032
title: "Why is `unique_ptr` considered the default smart pointer for embedded?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
  - source_id: cpp-draft-unique-ptr-dltr-dflt
    title: "C++ working draft: default_delete ([unique.ptr.dltr.dflt])"
    url: https://eel.is/c++draft/unique.ptr.dltr.dflt
  - source_id: cppcg-r21
    title: "C++ Core Guidelines: R.21 – Prefer unique_ptr over shared_ptr unless you need to share ownership"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r21-prefer-unique_ptr-over-shared_ptr-unless-you-need-to-share-ownership
  - source_id: cpp-draft-util-smartptr-shared-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
---

## Short answer

**Raw-pointer-level access, exclusive ownership, explicit transfer via move, custom deleter support for HAL.**

A `unique_ptr` with the default deleter stores a pointer and a `default_delete` with no data members, so in typical implementations its size equals a raw pointer's; `*` and `->` dereference that same pointer.[^cpp-draft-unique-ptr-dltr-dflt][^cpp-draft-unique-ptr-single] For most ownership cases that is enough: unlike `shared_ptr`, it keeps no reference count.[^cppcg-r21]

Rule: start with `unique_ptr`; move to `shared_ptr` only when shared ownership is genuinely needed.[^embeddedinterviewlab]

## Detailed explanation

TODO
