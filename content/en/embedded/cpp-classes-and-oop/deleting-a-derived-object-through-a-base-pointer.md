---
id: emb-cppoop-0017
title: "Why does a base class with virtual methods need a virtual destructor?"
description: "Without a virtual destructor, deleting a derived object through a base pointer is undefined behavior"
track: embedded
section: cpp-classes-and-oop
level: junior
type: pitfall
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
  - source_id: cpp-draft-expr-delete
    title: "C++ working draft: Delete ([expr.delete])"
    url: https://eel.is/c++draft/expr.delete
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraph 3: in a single-object delete-expression, if the static type is not similar to the dynamic type, the static type must be a base class of the dynamic type and must have a virtual destructor, otherwise the behavior is undefined. It does not describe what a particular compiler does."
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraph 15: for a virtual destructor the deallocation function is determined as if `delete this` appeared in a non-virtual destructor of that class, which ensures a deallocation function matching the dynamic type of the object is available. It does not apply to non-virtual destructors."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Section 2.5.2 says a virtual destructor takes a pair of vtable entries: the complete object destructor (no delete) and the deleting destructor (destroys the object and calls delete). This is an ABI, not the language standard."
  - source_id: cpp-core-guidelines-c35
    title: "C++ Core Guidelines: C.35 (base class destructor)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c35-a-base-class-destructor-should-be-either-public-and-virtual-or-protected-and-non-virtual
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Rule C.35: a base class destructor should be either public and virtual, or protected and non-virtual; protected prevents deletion through a base pointer. This is a style recommendation, not a language requirement."
  - source_id: cpp-core-guidelines-c127
    title: "C++ Core Guidelines: C.127 (virtual or protected destructor)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c127-a-class-with-a-virtual-function-should-have-a-virtual-or-protected-destructor
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Rule C.127: a class with a virtual function should have a virtual or protected destructor; its `unique_ptr<B>` holding a `D` without such a destructor is called undefined behavior. This is a style recommendation, not a language requirement."
---

## Short answer

<span class="warn">Without a virtual destructor, deleting a derived object through a `Base*` is undefined behavior.</span>[^cpp-draft-expr-delete]

In practice `Base* p = new Derived; delete p;` usually calls only `~Base()`, so the derived resources are not freed, but the standard does not guarantee even that. Protection: if a class has virtual functions and may be deleted through a base pointer, declare `virtual ~Base()`; if such deletion is not intended, make the destructor protected and non-virtual.[^cpp-core-guidelines-c35]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
