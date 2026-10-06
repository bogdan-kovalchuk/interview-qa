---
id: emb-raii-0012
title: "When is `shared_ptr` nevertheless justified in embedded?"
description: "When there is genuine shared ownership and the cost of the control block and counters is acceptable; the default needs the heap, but `allocate_shared` lets you supply your own allocator."
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
    applicability: "Describes the libstdc++ implementation: counter policies atomic (when an atomic compare-and-swap builtin exists), mutex (without atomic builtins) and single (library built without threads); make_shared forwards to allocate_shared with std::allocator; shared_ptr offers the same level of thread safety as built-in types. Applies to libstdc++ only; other libraries can differ."
  - source_id: cpp-draft-util-smartptr-shared
    title: "C++ working draft: Class template shared_ptr ([util.smartptr.shared])"
    url: https://eel.is/c++draft/util.smartptr.shared
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that shared_ptr implements shared ownership and that the last remaining owner is responsible for destroying the object; that, for determining data races, member functions access only the shared_ptr and weak_ptr objects themselves and not the objects they refer to. Does not advise when to use it."
  - source_id: cpp-draft-util-smartptr-shared-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that allocate_shared allocates memory using a copy of the supplied allocator, and that implementations of make_shared and allocate_shared should perform no more than one memory allocation. Does not describe how to build a pool allocator."
  - source_id: cppcg-r21
    title: "C++ Core Guidelines: R.21 – Prefer unique_ptr over shared_ptr unless you need to share ownership"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r21-prefer-unique_ptr-over-shared_ptr-unless-you-need-to-share-ownership
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: unique_ptr is simpler, more predictable (you know when destruction happens) and faster because it keeps no use count; a shared_ptr whose count never exceeds 1 maintains it needlessly. Says nothing about specific embedded scenarios."
  - source_id: cppcg-r24
    title: "C++ Core Guidelines: R.24 – Use std::weak_ptr to break cycles of shared_ptrs"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r24-use-stdweak_ptr-to-break-cycles-of-shared_ptrs
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: shared_ptrs rely on use counting, and the use count of a cyclic structure never reaches zero, so cycles must be broken with weak_ptr. Says nothing about cost or the embedded context."
---

## Short answer

**When there is genuine shared ownership – no single owner outlives all the users – and the cost of the control block and counters is acceptable.**

Examples: reference-counted buffers in embedded Linux userspace, plugin and modular systems with shared config blocks, objects whose lifetime truly has no single owner. `make_shared` allocates through `std::allocator` by default,[^libstdcxx-memory] while `allocate_shared` accepts your own allocator.[^cpp-draft-util-smartptr-shared-create] For DMA (direct memory access) buffers in bare-metal, an explicit owner plus borrowed views is usually better.

Rule: `shared_ptr` is only for real shared ownership, not just in case.[^cppcg-r21]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
