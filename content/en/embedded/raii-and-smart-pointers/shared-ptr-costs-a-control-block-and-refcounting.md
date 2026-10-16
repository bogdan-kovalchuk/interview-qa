---
id: emb-raii-0010
title: "Why is `shared_ptr` rarely used in embedded?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-shared-ptr-general
    title: "C++ working draft: shared_ptr, General ([util.smartptr.shared.general])"
    url: https://eel.is/c++draft/util.smartptr.shared.general
  - source_id: cpp-draft-shared-ptr-const
    title: "C++ working draft: shared_ptr constructors ([util.smartptr.shared.const])"
    url: https://eel.is/c++draft/util.smartptr.shared.const
  - source_id: cpp-draft-shared-ptr-dest
    title: "C++ working draft: shared_ptr destructor ([util.smartptr.shared.dest])"
    url: https://eel.is/c++draft/util.smartptr.shared.dest
  - source_id: cpp-draft-shared-ptr-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
  - source_id: cpp-draft-shared-ptr-obs
    title: "C++ working draft: shared_ptr observers ([util.smartptr.shared.obs])"
    url: https://eel.is/c++draft/util.smartptr.shared.obs
  - source_id: cpp-draft-memory-syn
    title: "C++ working draft: Header <memory> synopsis ([memory.syn])"
    url: https://eel.is/c++draft/memory.syn
  - source_id: cpp-draft-freestanding-item
    title: "C++ working draft: Freestanding items ([freestanding.item])"
    url: https://eel.is/c++draft/freestanding.item
  - source_id: cppcg-r21-prefer-unique-ptr
    title: "C++ Core Guidelines: R.21 – Prefer unique_ptr over shared_ptr unless you need to share ownership"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r21-prefer-unique_ptr-over-shared_ptr-unless-you-need-to-share-ownership
---

## Short answer

<span class="warn">Expensive: a shared control block, reference counting on copy/assign/destroy, and usually heap allocation.</span> The constructor taking a pointer can throw `bad_alloc`, and for `make_shared` the standard recommends at most one allocation.[^cpp-draft-shared-ptr-const][^cpp-draft-shared-ptr-create] The last owner destroys the object, so the moment of destruction is not visible from local code.[^cpp-draft-shared-ptr-general] Rule: on bare metal without a heap, avoid `shared_ptr`; for a single owner, use `unique_ptr`.[^cppcg-r21-prefer-unique-ptr]

## Detailed explanation

TODO
