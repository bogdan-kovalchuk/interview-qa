---
id: emb-raii-0011
title: "What are the concrete costs of `shared_ptr`?"
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
  - source_id: cppcg-r22
    title: "C++ Core Guidelines: R.22 – Use make_shared() to make shared_ptrs"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r22-use-make_shared-to-make-shared_ptrs
---

## Short answer

**A control block with counters, usually atomic increments/decrements, dynamic allocation, and destruction when the last owner lets go.**

In libstdc++, a `shared_ptr` holds pointers to the object and to a control block (strong/weak counters, deleter/allocator state); counters use atomic operations (cheaper non-atomic ones if single-threaded).[^libstdcxx-memory] The standard recommends that `make_shared` do at most one allocation, but the control block remains.[^cpp-draft-util-smartptr-shared-create]

Rule: name the cost categories, not just "shared_ptr is slow"; for one owner, `unique_ptr` is simpler and faster.[^cppcg-r21]

## Detailed explanation

TODO
