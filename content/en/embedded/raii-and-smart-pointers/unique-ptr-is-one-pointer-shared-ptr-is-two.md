---
id: emb-raii-0022
title: "How do `unique_ptr` and `shared_ptr` differ in size?"
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
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: Object model ([intro.object])"
    url: https://eel.is/c++draft/intro.object
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: libstdcxx-memory
    title: "The GNU C++ Library Manual: Memory – shared_ptr"
    url: https://gcc.gnu.org/onlinedocs/libstdc++/manual/memory.html#std.util.memory.shared_ptr
  - source_id: cpp-draft-util-smartptr-shared-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
---

## Short answer

**`unique_ptr` (with a stateless deleter) is usually the size of a raw pointer; `shared_ptr` is usually two pointers plus a separate control block.**

`shared_ptr` stores a pointer to the object and one to the control block with the counters; in libstdc++, `make_shared` uses one allocation for both.[^libstdcxx-memory] The exact size depends on the STL and ABI: under the Itanium C++ ABI, an empty base may sit at offset zero.[^itanium-cxx-abi]

Rule: one owner -> `unique_ptr`; shared ownership -> `shared_ptr`, if its control block and counters are acceptable.[^libstdcxx-memory]

## Detailed explanation

TODO
