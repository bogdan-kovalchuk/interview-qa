---
id: emb-cppoop-0003
title: "What is the implicit `this` pointer?"
description: "A pointer to the object a non-static member function was called on; conceptually a hidden first parameter."
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
  - source_id: cpp-draft-expr-prim-this
    title: "C++ working draft: This ([expr.prim.this])"
    url: https://eel.is/c++draft/expr.prim.this
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines this as a prvalue pointer to the object a non-static member function was called on, with its cv-qualification; does not describe how a compiler passes that pointer."
  - source_id: cpp-draft-over-match-funcs
    title: "C++ working draft: Candidate functions and argument lists ([over.match.funcs.general])"
    url: https://eel.is/c++draft/over.match.funcs.general
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Describes the implicit object parameter as an extra first parameter for overload resolution; the standard says explicitly this is only a descriptive model, not a requirement on implementations."
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Supports only that virtual functions provide dynamic binding; the standard does not specify the mechanism (vtable)."
---

## Short answer

**`this` is a pointer to the object for which a non-static member function was called.**[^cpp-draft-expr-prim-this] For overload resolution the standard models it as an extra first parameter, so `obj.set()` works roughly like a call receiving `&obj`.[^cpp-draft-over-match-funcs] The type of `this` is `X*`, or `const X*` inside a `const` member function; a `static` member function has no `this`. For a non-`virtual` method this is close to a C function with an explicit struct pointer; the optimizer often removes the difference, but the standard does not guarantee it.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
