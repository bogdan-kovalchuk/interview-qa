---
id: cpp-ptrref-0001
title: "unique_ptr or shared_ptr: how do you choose between them?"
description: "Exclusive ownership is the default; shared ownership adds shared-lifetime bookkeeping."
track: cpp
section: pointers-and-references
level: middle
type: comparison
tags: [smart-pointers, ownership, raii, lifetime]
status: published
updated: 2026-09-08
content_revision: 3
reconciled_with:
  uk: 3
applies_to:
  - product: ISO C++
    version: "C++20"
anki:
  export: true
sources:
  - source_id: cpp-draft-smartptr
    title: "C++ working draft: smart pointers ([smartptr])"
    url: https://eel.is/c++draft/smartptr
    accessed: 2026-09-04
    kind: spec
    version: "C++20"
    applicability: ownership semantics and stored deleter; the standard specifies behaviour, not object layout
  - source_id: cppreference-unique-ptr
    title: "cppreference: std::unique_ptr"
    url: https://en.cppreference.com/w/cpp/memory/unique_ptr
    accessed: 2026-09-03
    kind: community
    version: "C++20"
    applicability: "Move-only semantics, deleter storage, and common implementation characteristics through C++20; object size is not guaranteed."
  - source_id: cppreference-shared-ptr
    title: "cppreference: std::shared_ptr"
    url: https://en.cppreference.com/w/cpp/memory/shared_ptr
    accessed: 2026-09-03
    kind: community
    version: "C++20"
    applicability: "Shared ownership, control-block implementations, thread-safety rules, and common make_shared allocation behaviour through C++20."
---

## Short answer

**Use `unique_ptr` unless the lifetime genuinely has several independent owners.** It is move-only
and stores a pointer together with its deleter; the standard does not guarantee raw-pointer size or
zero runtime cost.[^cpp-draft-smartptr] `shared_ptr` shares ownership through bookkeeping commonly
held in a control block. Copies may require synchronization, while the pointee itself gets no thread
safety. The object is destroyed when the last owner releases it; ownership cycles require
`weak_ptr`.[^cppreference-shared-ptr]

## Detailed explanation

Both types express ownership, and the difference is how many owners there may be.

`unique_ptr` states that exactly one owner exists at a time. It cannot be copied, only moved, and that
restriction is what makes the ownership readable in the signature: a function taking `unique_ptr<T>`
by value takes ownership, and one taking `T*` or `T&` borrows. With the default deleter it is
typically represented as one pointer, and destruction invokes the stored deleter directly. Neither
layout nor zero overhead is a C++ guarantee.[^cpp-draft-smartptr] A stateful deleter, such as a
captured lambda or a function pointer, is stored as part of the smart pointer and can add size or
invocation cost.

`shared_ptr` states that ownership is shared and the last owner cleans up. That requires a control
block that implementations commonly use for ownership counts and the deleter. Those counts commonly
use atomic operations. The standard guarantees that different `shared_ptr` objects sharing ownership
can be used concurrently without a data race on the ownership machinery, but the pointee itself gets
no protection: two threads writing to it can still race.[^cpp-draft-smartptr] Implementations commonly
let `make_shared` allocate the control block and object together; that can save an allocation but can
keep the combined storage alive while a `weak_ptr` remains.[^cppreference-shared-ptr]

```cpp
struct Node {
    std::unique_ptr<Node> next;      // exclusive: the list owns its tail
    std::shared_ptr<Config> config;  // shared: many nodes read one config
    std::weak_ptr<Node> parent;      // observing: breaks the ownership cycle
};
```

The costly mistake is not one counter update; it is losing the answer to "who deletes this, and
when". A graph of `shared_ptr` owners destroys an object when and where the last owner releases it,
which may be a different thread from the creator. An ownership cycle releases nothing at all.

## Comparison

| | `unique_ptr` | `shared_ptr` |
|---|---|---|
| Owners | exactly one | any number |
| Copyable | no, move-only | yes |
| Typical representation | often one pointer | often two pointers plus a control block |
| Extra allocation | none required by ownership | control block; often combined by `make_shared` |
| Cost of copy | move pointer and deleter | shared-ownership bookkeeping, often synchronized |
| Destruction point | deterministic, at scope exit | wherever the last owner releases |
| Cycles | impossible | possible, broken by `weak_ptr` |
| Thread safety | none needed | the count only, never the object |

## When to choose which

Choose `unique_ptr` for a member that a class owns, for a factory return value, for pimpl, and for any
transfer of ownership across an API boundary. It is the default because it documents the lifetime
and avoids shared-ownership bookkeeping.

Choose `shared_ptr` when the number of owners genuinely is not known at compile time: a cache handed
to several subsystems, a node in a graph that outlives the traversal that found it, an object captured
by an asynchronous callback that may complete after its creator is gone. Take it by value only when
the callee stores it; otherwise take a reference or a raw pointer, because borrowing does not require
ownership.

Use `weak_ptr` where an observer must not keep the object alive, and check by locking it rather than
by testing expiry, since the object can die between the two calls.

## Evaluation guide

### Expected signals

- Names exclusive versus shared ownership as the deciding question, not performance.
- Knows `unique_ptr` is move-only and distinguishes common zero-overhead implementations from a
  standard guarantee.
- Knows shared ownership needs bookkeeping, commonly with atomic counters, and that it does not
  protect the pointee.
- Brings up cycles and `weak_ptr` without being prompted.

### Red flags

- "`shared_ptr` is safer, so use it everywhere."
- Believes a `shared_ptr` makes the pointed-to object thread-safe.
- Passes `shared_ptr` by value into functions that only read the object, and cannot say what that
  costs.

### Level-up follow-up

Ask what changes if the last reference is dropped on a different thread than the one that created the
object, and how they would keep destruction on a chosen thread.

## Sources

<!-- generated from frontmatter -->
