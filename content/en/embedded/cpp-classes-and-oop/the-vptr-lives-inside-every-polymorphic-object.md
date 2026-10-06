---
id: emb-cppoop-0015
title: "What is the vptr and where is it stored?"
description: "A hidden pointer inside every object with virtual functions, pointing at the vtable of its dynamic type"
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
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines a polymorphic class and explains in a note that a virtual call depends on the dynamic type of the object while a non-virtual call depends on the static type; this clause does not mention a vptr."
  - source_id: cpp-draft-class-cdtor
    title: "C++ working draft: Construction and destruction ([class.cdtor])"
    url: https://eel.is/c++draft/class.cdtor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraph 4: a virtual call from a constructor or destructor on the object under construction selects the final overrider in that constructor's class, not in a more derived one. It does not say how this is implemented (vptr)."
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: Copy/move constructors ([class.copy.ctor])"
    url: https://eel.is/c++draft/class.copy.ctor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraph 12: a copy/move constructor of a class with virtual functions or virtual bases is not trivial. By itself it says nothing about the vptr or about what memcpy does."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "Sections 2.4 and 2.6 define a dynamic class (virtual functions or virtual bases), the vptr at offset 0 when there is no primary base, and the rule that during construction the object assumes the type of each base in turn, with the vptr set to that base's table. This is an ABI, not the language standard; other ABIs may place the vptr differently."
---

## Short answer

**A vptr is a hidden pointer inside every object with virtual functions, pointing at the vtable of its dynamic type.** The compiler typically adds it as a hidden member, so `sizeof` grows by about one pointer (4 bytes on 32-bit, subject to alignment). Its position is ABI-dependent, not set by the C++ standard; the Itanium C++ ABI uses offset 0 when the class has no primary base. Only the first virtual function in a hierarchy adds a vptr; later ones do not grow the object.[^itanium-cxx-abi]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
