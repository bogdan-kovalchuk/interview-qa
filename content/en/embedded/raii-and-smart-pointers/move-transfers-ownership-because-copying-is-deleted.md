---
id: emb-raii-0009
title: "How do you transfer ownership of a resource through a `unique_ptr`?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-unique-ptr-general
    title: "C++ working draft: Unique-ownership pointers, General ([unique.ptr.general])"
    url: https://eel.is/c++draft/unique.ptr.general
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
  - source_id: cpp-draft-forward
    title: "C++ working draft: forward/move ([forward])"
    url: https://eel.is/c++draft/forward
  - source_id: cppcg-r32-sink-unique-ptr
    title: "C++ Core Guidelines: R.32 – Take a unique_ptr<widget> parameter to express that a function assumes ownership of a widget"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r32-take-a-unique_ptrwidget-parameter-to-express-that-a-function-assumes-ownership-of-a-widget
  - source_id: cppcg-f48-dont-return-move-local
    title: "C++ Core Guidelines: F.48 – Don’t return std::move(local)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#f48-dont-return-stdmovelocal
---

## Short answer

**Via `std::move()` – copying is deleted, the transfer is explicit.** `auto b = std::move(a);` transfers ownership: `a` becomes empty (`a.get() == nullptr`) and `b` is now responsible for releasing the resource.[^cpp-draft-unique-ptr-single] `std::move` itself only casts the expression to an rvalue; the transfer is done by the `unique_ptr` move constructor or move assignment.[^cpp-draft-forward] Rule: `unique_ptr` is move-only; an explicit `std::move` documents who owns the resource now, and a value returned from a function needs no `std::move`.[^cppcg-f48-dont-return-move-local]

## Detailed explanation

TODO
