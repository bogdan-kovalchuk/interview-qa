---
id: emb-raii-0011
title: "What are the concrete costs of `shared_ptr`?"
description: "A shared pointer costs a control block with strong and weak counters, usually atomic count updates, dynamic allocation (a single block with `make_shared`), and a destruction moment set by the last owner."
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
  - source_id: libstdcxx-memory
    title: "The GNU C++ Library Manual: Memory – shared_ptr"
    url: https://gcc.gnu.org/onlinedocs/libstdc++/manual/memory.html#std.util.memory.shared_ptr
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "Describes the libstdc++ implementation: shared_ptr holds a pointer to the object and a pointer to a control block; the control block keeps the strong/weak counters, while derived classes store the deleter and allocator; counters are updated with atomic operations (atomic, mutex and single lock policies), or cheaper non-atomic ones in a single-threaded program; make_shared can place the object and the control block in one block. Applies to libstdc++ only; other libraries can differ."
  - source_id: cpp-draft-util-smartptr-shared
    title: "C++ working draft: Class template shared_ptr ([util.smartptr.shared])"
    url: https://eel.is/c++draft/util.smartptr.shared
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that the last remaining owner is responsible for destroying the object; that, for determining data races, member functions access only the shared_ptr and weak_ptr objects themselves and not the objects they refer to; and that changes in use_count() do not reflect modifications that can introduce data races. Does not specify the control block layout or the cost of operations."
  - source_id: cpp-draft-util-smartptr-shared-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that implementations of make_shared and allocate_shared should perform no more than one memory allocation, that allocate_shared uses a copy of the supplied allocator, and that these functions typically allocate more than sizeof(T) for bookkeeping such as reference counts. Does not guarantee a single block."
  - source_id: cppcg-r21
    title: "C++ Core Guidelines: R.21 – Prefer unique_ptr over shared_ptr unless you need to share ownership"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r21-prefer-unique_ptr-over-shared_ptr-unless-you-need-to-share-ownership
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: unique_ptr is simpler, more predictable (you know when destruction happens) and faster because it keeps no use count; a shared_ptr whose count never exceeds 1 maintains it needlessly. A guideline, not a performance measurement."
  - source_id: cppcg-r22
    title: "C++ Core Guidelines: R.22 – Use make_shared() to make shared_ptrs"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r22-use-make_shared-to-make-shared_ptrs
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: make_shared can eliminate a separate allocation for the reference counts by placing them next to the object; it also gives exception safety in complex expressions before C++17. Says nothing about the size or cost of the counters."
---

## Short answer

**A control block with counters, usually atomic increments/decrements, dynamic allocation, and destruction when the last owner lets go.**

In libstdc++, a `shared_ptr` holds pointers to the object and to a control block (strong/weak counters, deleter/allocator state); counters use atomic operations (cheaper non-atomic ones if single-threaded).[^libstdcxx-memory] The standard recommends that `make_shared` do at most one allocation, but the control block remains.[^cpp-draft-util-smartptr-shared-create]

Rule: name the cost categories, not just "shared_ptr is slow"; for one owner, `unique_ptr` is simpler and faster.[^cppcg-r21]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
