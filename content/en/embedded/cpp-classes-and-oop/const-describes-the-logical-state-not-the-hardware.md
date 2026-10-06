---
id: emb-cppoop-0005
title: "Why are hardware access methods often marked `const` even though they change a register?"
description: "const refers to the logical state of the object (its fields), not the hardware its pointer refers to."
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
  - source_id: cpp-draft-expr-ref
    title: "C++ working draft: Class member access ([expr.ref])"
    url: https://eel.is/c++draft/expr.ref
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines the type of E1.E2 for a non-static member: the object's cv-qualification is added to the member's type (except mutable); says nothing about what a pointer member points to."
  - source_id: cpp-draft-dcl-type-cv
    title: "C++ working draft: The cv-qualifiers ([dcl.type.cv])"
    url: https://eel.is/c++draft/dcl.type.cv
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that a const-qualified access path cannot be used to modify an object and that modifying a const object is undefined behavior; explains the difference between a const pointer and a pointer to const. Does not say which methods should be marked const."
  - source_id: cpp-draft-expr-assign
    title: "C++ working draft: Assignment and compound assignment operators ([expr.assign])"
    url: https://eel.is/c++draft/expr.assign
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Requires a modifiable lvalue as the left operand of assignment and compound assignment; this is why modifying a field in a const method is a compile error."
  - source_id: cppcg-con2-const-members
    title: "C++ Core Guidelines: Con.2 – By default, make member functions const"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#con2-by-default-make-member-functions-const
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Design guidance: mark a method const if it does not change the object's observable state; notes explicitly that a const method can change what is reachable through a pointer member. A guideline, not a language requirement."
---

## Short answer

**`const` refers to the logical state of the object (its fields), not the hardware.** In a `const` method the members become `const`, so `odr_` is `volatile uint32_t *const`: the pointer is immutable, but what it points to is not, so writing the register through it is allowed.[^cpp-draft-expr-ref][^cpp-draft-dcl-type-cv] The Core Guidelines advise marking a method `const` when it does not change the object's observable state, and allow modification through a pointer member.[^cppcg-con2-const-members] Whether a register write changes the handle's "state" is a design decision, not a language rule.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
