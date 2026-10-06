---
id: emb-raii-0010
title: "Why is `shared_ptr` rarely used in embedded?"
description: "Expensive: a shared control block, reference counting on copy, assign and destroy, and usually a heap allocation."
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
  - source_id: cpp-draft-shared-ptr-general
    title: "C++ working draft: shared_ptr, General ([util.smartptr.shared.general])"
    url: https://eel.is/c++draft/util.smartptr.shared.general
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Says shared_ptr implements shared ownership and that the last remaining owner is responsible for destroying the object; changes in `use_count()` are not counted when determining a data race. Does not describe the internal structure of a control block or say whether the count is atomic."
  - source_id: cpp-draft-shared-ptr-const
    title: "C++ working draft: shared_ptr constructors ([util.smartptr.shared.const])"
    url: https://eel.is/c++draft/util.smartptr.shared.const
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "The constructors taking a pointer or a deleter can throw `bad_alloc`; the allocator versions use a copy of the allocator for memory for internal use. Does not call that memory a control block and does not fix its size."
  - source_id: cpp-draft-shared-ptr-dest
    title: "C++ working draft: shared_ptr destructor ([util.smartptr.shared.dest])"
    url: https://eel.is/c++draft/util.smartptr.shared.dest
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Says the destructor has no side effects if the shared_ptr is empty or shares ownership with another one, and otherwise calls the deleter or `delete` on the pointer. Says nothing about the cost of the count."
  - source_id: cpp-draft-shared-ptr-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "`make_shared` and `allocate_shared` allocate memory for the object and throw `bad_alloc` or an exception from allocate; `allocate_shared` uses a copy of the given allocator; implementations should perform no more than one allocation (should). Does not guarantee a single allocation."
  - source_id: cpp-draft-shared-ptr-obs
    title: "C++ working draft: shared_ptr observers ([util.smartptr.shared.obs])"
    url: https://eel.is/c++draft/util.smartptr.shared.obs
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "A note on `use_count()`: when multiple threads might change the value, the result is approximate, and `use_count() == 1` does not imply that accesses through a previously destroyed shared_ptr have completed."
  - source_id: cpp-draft-memory-syn
    title: "C++ working draft: Header <memory> synopsis ([memory.syn])"
    url: https://eel.is/c++draft/memory.syn
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "In the synopsis `unique_ptr` is marked with a freestanding comment, while `shared_ptr` and `weak_ptr` carry no such mark. This is the state of the working draft, not of already shipped toolchains."
  - source_id: cpp-draft-freestanding-item
    title: "C++ working draft: Freestanding items ([freestanding.item])"
    url: https://eel.is/c++draft/freestanding.item
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Explains that a synopsis declaration marked freestanding is required in a freestanding implementation as well. Does not describe what a particular toolchain ships."
  - source_id: cppcg-r21-prefer-unique-ptr
    title: "C++ Core Guidelines: R.21 – Prefer unique_ptr over shared_ptr unless you need to share ownership"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r21-prefer-unique_ptr-over-shared_ptr-unless-you-need-to-share-ownership
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "A guideline: unique_ptr is simpler, more predictable and faster because it keeps no use count. It is a recommendation, not a language requirement, and does not apply when ownership is truly shared."
---

## Short answer

<span class="warn">Expensive: a shared control block, reference counting on copy/assign/destroy, and usually heap allocation.</span> The constructor taking a pointer can throw `bad_alloc`, and for `make_shared` the standard recommends at most one allocation.[^cpp-draft-shared-ptr-const][^cpp-draft-shared-ptr-create] The last owner destroys the object, so the moment of destruction is not visible from local code.[^cpp-draft-shared-ptr-general] Rule: on bare metal without a heap, avoid `shared_ptr`; for a single owner, use `unique_ptr`.[^cppcg-r21-prefer-unique-ptr]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
