---
id: emb-cppoop-0029
title: "How does a static member function differ from an ordinary one?"
description: "A static member function has no this pointer and is not bound to an instance, making it useful as a C callback thunk"
track: embedded
section: cpp-classes-and-oop
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
  - source_id: cpp-draft-class-static
    title: "C++ working draft: Static members ([class.static])"
    url: https://eel.is/c++draft/class.static
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that a static member can be named as X::s without an object (or through an object expression that is evaluated), and that a static member function has no this and cannot be const, volatile or virtual. Does not describe how a compiler calls such a function."
  - source_id: cpp-draft-expr-prim-this
    title: "C++ working draft: This ([expr.prim.this])"
    url: https://eel.is/c++draft/expr.prim.this
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines this as a prvalue pointer to the object a non-static member function was called on, with its cv-qualification; does not describe how a compiler passes that pointer."
  - source_id: cpp-draft-expr-unary-op
    title: "C++ working draft: Unary operators ([expr.unary.op])"
    url: https://eel.is/c++draft/expr.unary.op
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that & applied to a qualified-id naming a non-static member yields a pointer to member, and otherwise an ordinary \"pointer to T\", so a static and a non-static function give different types (pointer to function versus pointer to member function). Says nothing about language linkage."
  - source_id: cpp-draft-dcl-link
    title: "C++ working draft: Linkage specifications ([dcl.link])"
    url: https://eel.is/c++draft/dcl.link
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that function types have C++ language linkage by default and that function types with different language linkages are distinct types. Does not assess how individual compilers accept or reject that difference in practice."
---

## Short answer

**A static member function has no `this`** – it is not bound to an instance.[^cpp-draft-class-static] So it can be called as `Class::func()` without an object, but it cannot directly touch non-static members. Its address is an ordinary function pointer, not a pointer to member,[^cpp-draft-expr-unary-op] so it is often used as a callback thunk for a C API (application programming interface), passing the object through a `void*` context. Function types have a language linkage, so strict C compatibility sometimes needs a separate `extern "C"` wrapper function.[^cpp-draft-dcl-link]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
