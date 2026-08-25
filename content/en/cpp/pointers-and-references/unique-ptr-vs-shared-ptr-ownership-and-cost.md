---
id: cpp-ptrref-0001
title: "unique_ptr or shared_ptr: how do you choose between them?"
description: "Exclusive ownership is the default; shared ownership buys a control block and atomic counters."
track: cpp
section: pointers-and-references
level: middle
type: comparison
tags: [smart-pointers, ownership, raii, lifetime]
status: published
updated: 2026-09-03
content_revision: 1
reconciled_with:
  uk: 1
applies_to:
  - product: ISO C++
    version: "C++20"
anki:
  export: true
sources:
  - source_id: cppreference-unique-ptr
    title: "cppreference: std::unique_ptr"
    url: https://en.cppreference.com/w/cpp/memory/unique_ptr
    accessed: 2026-09-03
    kind: spec
    version: "C++20"
    applicability: "Move-only semantics, deleter storage and size guarantees through C++20."
  - source_id: cppreference-shared-ptr
    title: "cppreference: std::shared_ptr"
    url: https://en.cppreference.com/w/cpp/memory/shared_ptr
    accessed: 2026-09-03
    kind: spec
    version: "C++20"
    applicability: "Control block, thread safety of the reference count and make_shared allocation behaviour through C++20."
---

## Short answer

**Use `unique_ptr` unless the lifetime genuinely has several independent owners.** `unique_ptr` is
move-only and, with a stateless deleter, costs the same as a raw pointer.[^cppreference-unique-ptr]
`shared_ptr` adds a control block with atomic strong and weak counts, so every copy and destruction is
an atomic operation and the object dies at an unpredictable point.[^cppreference-shared-ptr] Shared
ownership also admits reference cycles, which `weak_ptr` exists to break. Reaching for `shared_ptr`
first is usually a sign that ownership was never decided.

## Detailed explanation

Both types express ownership, and the difference is how many owners there may be.

`unique_ptr` states that exactly one owner exists at a time. It cannot be copied, only moved, and that
restriction is what makes the ownership readable in the signature: a function taking `unique_ptr<T>`
by value takes ownership, and one taking `T*` or `T&` borrows. With the default deleter the object is
the size of one pointer and destruction is a direct `delete`, so there is nothing to pay for at run
time.[^cppreference-unique-ptr] A stateful deleter, such as a captured lambda or a function pointer,
is stored inside and does add size.

`shared_ptr` states that ownership is shared and the last owner cleans up. That requires a control
block holding the strong count, the weak count and the deleter. The counts are updated atomically,
which makes copying a `shared_ptr` safe from several threads but not free, and the pointee itself
receives no protection whatsoever: two threads writing to the same object through two `shared_ptr`
copies is still a data race.[^cppreference-shared-ptr] `make_shared` allocates the control block and
the object together, which saves one allocation but keeps the object's storage alive as long as any
`weak_ptr` exists.

```cpp
struct Node {
    std::unique_ptr<Node> next;      // exclusive: the list owns its tail
    std::shared_ptr<Config> config;  // shared: many nodes read one config
    std::weak_ptr<Node> parent;      // observing: breaks the ownership cycle
};
```

The costly mistake is not the atomic increment; it is losing the answer to "who deletes this, and
when". A graph of `shared_ptr` owners deletes objects at whichever thread happens to drop the last
reference, at a point no one wrote down, and a cycle deletes nothing at all.

## Comparison

| | `unique_ptr` | `shared_ptr` |
|---|---|---|
| Owners | exactly one | any number |
| Copyable | no, move-only | yes |
| Size, default deleter | one pointer | two pointers |
| Extra allocation | none | control block, merged by `make_shared` |
| Cost of copy | pointer move | atomic increment |
| Destruction point | deterministic, at scope exit | wherever the last owner releases |
| Cycles | impossible | possible, broken by `weak_ptr` |
| Thread safety | none needed | the count only, never the object |

## When to choose which

Choose `unique_ptr` for a member that a class owns, for a factory return value, for pimpl, and for any
transfer of ownership across an API boundary. It is the default because it documents the lifetime and
costs nothing.

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
- Knows `unique_ptr` is move-only and, with the default deleter, has no space or time overhead over a
  raw pointer.
- Knows the control block is atomic, and that this protects the count and not the object.
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
