---
id: emb-raii-0022
title: "How do `unique_ptr` and `shared_ptr` differ in size?"
description: "`unique_ptr` with stateless deleter is usually the size of a raw pointer; `shared_ptr` is usually two pointers plus a separate control block."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-13; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says unique_ptr stores a pointer and a deleter, and its destructor calls the deleter only for a non-null pointer; copy operations are deleted and move is allowed. Does not fix the object's size."
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: Object model ([intro.object])"
    url: https://eel.is/c++draft/intro.object
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says a base subobject of a standard-layout class with no non-static data members has zero size, and that otherwise the circumstances of zero size are implementation-defined. Gives no sizeof values."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Class layout under the Itanium C++ ABI: an empty base is first placed at offset zero when possible. This is an ABI, not the C++ standard; vendor toolchains and other platforms can differ."
  - source_id: libstdcxx-memory
    title: "The GNU C++ Library Manual: Memory – shared_ptr"
    url: https://gcc.gnu.org/onlinedocs/libstdc++/manual/memory.html#std.util.memory.shared_ptr
    accessed: 2026-10-13
    kind: official
    version: "current"
    applicability: "Describes the libstdc++ implementation: shared_ptr holds a T* and a __shared_count pointing to _Sp_counted_base; make_shared places the object and control block in one allocation; counter updates use atomic operations or a mutex depending on the policy. Applies to libstdc++ only."
  - source_id: cpp-draft-util-smartptr-shared-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Says make_shared and allocate_shared should perform no more than one memory allocation; this is a recommendation, not a guarantee. Does not fix the control block layout."
---

## Short answer

**`unique_ptr` (with a stateless deleter) is usually the size of a raw pointer; `shared_ptr` is usually two pointers plus a separate control block.**

`shared_ptr` stores a pointer to the object and one to the control block with the counters; in libstdc++, `make_shared` uses one allocation for both.[^libstdcxx-memory] The exact size depends on the STL and ABI: under the Itanium C++ ABI, an empty base may sit at offset zero.[^itanium-cxx-abi]

Rule: one owner -> `unique_ptr`; shared ownership -> `shared_ptr`, if its control block and counters are acceptable.[^libstdcxx-memory]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
