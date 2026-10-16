---
id: emb-cppoop-0029
title: "How does a static member function differ from an ordinary one?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-static
    title: "C++ working draft: Static members ([class.static])"
    url: https://eel.is/c++draft/class.static
  - source_id: cpp-draft-expr-prim-this
    title: "C++ working draft: This ([expr.prim.this])"
    url: https://eel.is/c++draft/expr.prim.this
  - source_id: cpp-draft-expr-unary-op
    title: "C++ working draft: Unary operators ([expr.unary.op])"
    url: https://eel.is/c++draft/expr.unary.op
  - source_id: cpp-draft-dcl-link
    title: "C++ working draft: Linkage specifications ([dcl.link])"
    url: https://eel.is/c++draft/dcl.link
---

## Short answer

**A static member function has no `this`** – it is not bound to an instance.[^cpp-draft-class-static] So it can be called as `Class::func()` without an object, but it cannot directly touch non-static members. Its address is an ordinary function pointer, not a pointer to member,[^cpp-draft-expr-unary-op] so it is often used as a callback thunk for a C API (application programming interface), passing the object through a `void*` context. Function types have a language linkage, so strict C compatibility sometimes needs a separate `extern "C"` wrapper function.[^cpp-draft-dcl-link]

## Detailed explanation

TODO
