---
id: emb-raii-0012
title: "When is `shared_ptr` nevertheless justified in embedded?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: libstdcxx-memory
    title: "The GNU C++ Library Manual: Memory – shared_ptr"
    url: https://gcc.gnu.org/onlinedocs/libstdc++/manual/memory.html#std.util.memory.shared_ptr
  - source_id: cpp-draft-util-smartptr-shared
    title: "C++ working draft: Class template shared_ptr ([util.smartptr.shared])"
    url: https://eel.is/c++draft/util.smartptr.shared
  - source_id: cpp-draft-util-smartptr-shared-create
    title: "C++ working draft: shared_ptr creation ([util.smartptr.shared.create])"
    url: https://eel.is/c++draft/util.smartptr.shared.create
  - source_id: cppcg-r21
    title: "C++ Core Guidelines: R.21 – Prefer unique_ptr over shared_ptr unless you need to share ownership"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r21-prefer-unique_ptr-over-shared_ptr-unless-you-need-to-share-ownership
  - source_id: cppcg-r24
    title: "C++ Core Guidelines: R.24 – Use std::weak_ptr to break cycles of shared_ptrs"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r24-use-stdweak_ptr-to-break-cycles-of-shared_ptrs
---

## Short answer

**When there is genuine shared ownership – no single owner outlives all the users – and the cost of the control block and counters is acceptable.**

Examples: reference-counted buffers in embedded Linux userspace, plugin and modular systems with shared config blocks, objects whose lifetime truly has no single owner. `make_shared` allocates through `std::allocator` by default,[^libstdcxx-memory] while `allocate_shared` accepts your own allocator.[^cpp-draft-util-smartptr-shared-create] For DMA (direct memory access) buffers in bare-metal, an explicit owner plus borrowed views is usually better.

Rule: `shared_ptr` is only for real shared ownership, not just in case.[^cppcg-r21]

## Detailed explanation

TODO
