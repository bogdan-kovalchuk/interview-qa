---
id: emb-raii-0009
title: "How do you transfer ownership of a resource through a `unique_ptr`?"
description: "Ownership is transferred via std::move, which leaves the source empty and makes the new owner explicit in the code since `unique_ptr` is move-only."
track: embedded
section: raii-and-smart-pointers
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
  - source_id: cpp-draft-unique-ptr-general
    title: "C++ working draft: Unique-ownership pointers, General ([unique.ptr.general])"
    url: https://eel.is/c++draft/unique.ptr.general
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Says unique_ptr has strict ownership: it can be move-constructed and move-assigned but not copied. Says nothing about use in particular systems."
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines the deleted copy operations; the move constructor (afterwards the source's `get()` equals `nullptr` and the deleter is transferred); move assignment (`reset(u.release())`, then deleter assignment); the precondition `get() != nullptr` for `operator*` and `operator->`. Does not describe the behavior of a particular platform."
  - source_id: cpp-draft-forward
    title: "C++ working draft: forward/move ([forward])"
    url: https://eel.is/c++draft/forward
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Defines `std::move(t)` as `static_cast<remove_reference_t<T>&&>(t)`, that is, only a cast to an rvalue; the transfer itself is defined by the type's move constructor or move assignment."
  - source_id: cppcg-r32-sink-unique-ptr
    title: "C++ Core Guidelines: R.32 – Take a unique_ptr<widget> parameter to express that a function assumes ownership of a widget"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r32-take-a-unique_ptrwidget-parameter-to-express-that-a-function-assumes-ownership-of-a-widget
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "A guideline: a by-value `unique_ptr<widget>` parameter documents and enforces transfer of ownership to the function. A recommendation, not a language requirement."
  - source_id: cppcg-f48-dont-return-move-local
    title: "C++ Core Guidelines: F.48 – Don’t return std::move(local)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#f48-dont-return-stdmovelocal
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "A guideline: returning a local variable already moves it implicitly, and an explicit `std::move` prevents RVO, so it is a pessimization. A recommendation, not a language requirement."
---

## Short answer

**Via `std::move()` – copying is deleted, the transfer is explicit.** `auto b = std::move(a);` transfers ownership: `a` becomes empty (`a.get() == nullptr`) and `b` is now responsible for releasing the resource.[^cpp-draft-unique-ptr-single] `std::move` itself only casts the expression to an rvalue; the transfer is done by the `unique_ptr` move constructor or move assignment.[^cpp-draft-forward] Rule: `unique_ptr` is move-only; an explicit `std::move` documents who owns the resource now, and a value returned from a function needs no `std::move`.[^cppcg-f48-dont-return-move-local]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
