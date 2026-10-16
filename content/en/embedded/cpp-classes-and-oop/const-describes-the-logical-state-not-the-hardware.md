---
id: emb-cppoop-0005
title: "Why are hardware access methods often marked `const` even though they change a register?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-expr-ref
    title: "C++ working draft: Class member access ([expr.ref])"
    url: https://eel.is/c++draft/expr.ref
  - source_id: cpp-draft-dcl-type-cv
    title: "C++ working draft: The cv-qualifiers ([dcl.type.cv])"
    url: https://eel.is/c++draft/dcl.type.cv
  - source_id: cpp-draft-expr-assign
    title: "C++ working draft: Assignment and compound assignment operators ([expr.assign])"
    url: https://eel.is/c++draft/expr.assign
  - source_id: cppcg-con2-const-members
    title: "C++ Core Guidelines: Con.2 – By default, make member functions const"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#con2-by-default-make-member-functions-const
---

## Short answer

**`const` refers to the logical state of the object (its fields), not the hardware.** In a `const` method the members become `const`, so `odr_` is `volatile uint32_t *const`: the pointer is immutable, but what it points to is not, so writing the register through it is allowed.[^cpp-draft-expr-ref][^cpp-draft-dcl-type-cv] The Core Guidelines advise marking a method `const` when it does not change the object's observable state, and allow modification through a pointer member.[^cppcg-con2-const-members] Whether a register write changes the handle's "state" is a design decision, not a language rule.

## Detailed explanation

TODO
