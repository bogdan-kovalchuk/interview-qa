---
id: emb-cppoop-0003
title: "What is the implicit `this` pointer?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-expr-prim-this
    title: "C++ working draft: This ([expr.prim.this])"
    url: https://eel.is/c++draft/expr.prim.this
  - source_id: cpp-draft-over-match-funcs
    title: "C++ working draft: Candidate functions and argument lists ([over.match.funcs.general])"
    url: https://eel.is/c++draft/over.match.funcs.general
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
---

## Short answer

**`this` is a pointer to the object for which a non-static member function was called.**[^cpp-draft-expr-prim-this] For overload resolution the standard models it as an extra first parameter, so `obj.set()` works roughly like a call receiving `&obj`.[^cpp-draft-over-match-funcs] The type of `this` is `X*`, or `const X*` inside a `const` member function; a `static` member function has no `this`. For a non-`virtual` method this is close to a C function with an explicit struct pointer; the optimizer often removes the difference, but the standard does not guarantee it.

## Detailed explanation

TODO
