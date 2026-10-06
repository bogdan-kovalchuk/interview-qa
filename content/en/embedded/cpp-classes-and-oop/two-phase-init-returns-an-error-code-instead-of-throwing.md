---
id: emb-cppoop-0011
title: "How do you initialise an object when exceptions are disabled (`-fno-exceptions`)?"
description: "Two-phase init: a simple constructor that cannot fail plus a separate init() that returns an error code; the cost is an object that is not ready before init()."
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
  - source_id: cpp-draft-class-ctor-general
    title: "C++ working draft: Constructors ([class.ctor.general])"
    url: https://eel.is/c++draft/class.ctor.general
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "States that a constructor declaration allows only the decl-specifiers friend, inline, constexpr, consteval and explicit (so there is no return type) and that a return statement in a constructor body cannot specify a value. Does not say how to signal failure without exceptions."
  - source_id: cppcg-c41
    title: "C++ Core Guidelines: C.41 – A constructor should create a fully initialized object"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c41-a-constructor-should-create-a-fully-initialized-object
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: after the constructor the object should be usable; the example with an init() that must be called before other functions is shown as bad; exception: if a valid object cannot conveniently be constructed by a constructor, use a factory function. A guideline, not a requirement of the standard."
  - source_id: cppcg-c42
    title: "C++ Core Guidelines: C.42 – If a constructor cannot construct a valid object, throw an exception"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c42-if-a-constructor-cannot-construct-a-valid-object-throw-an-exception
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: throw an exception rather than leave an invalid object; for a variable definition there is no call from which an error code could be returned; for hard-real-time domains where exceptions are unpredictable it allows is_valid(), to be checked consistently and immediately; advises against post-constructor or two-stage initialization and, if unavoidable, to look at factory functions."
  - source_id: cppcg-c44
    title: "C++ Core Guidelines: C.44 – Prefer default constructors to be simple and non-throwing"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c44-prefer-default-constructors-to-be-simple-and-non-throwing
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: a default constructor should be simple and non-throwing so that setting a value to the default involves no operation that might fail. Says nothing about init()."
  - source_id: cppcg-e27
    title: "C++ Core Guidelines: E.27 – If you can't throw exceptions, use error codes systematically"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#e27-if-you-cant-throw-exceptions-use-error-codes-systematically
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: without exceptions use error codes systematically; shows returning a result together with an error indicator (a pair, a dedicated type) or a valid() on the object itself. Not a requirement of the standard."
  - source_id: cpp-draft-dcl-attr-nodiscard
    title: "C++ working draft: Nodiscard attribute ([dcl.attr.nodiscard])"
    url: https://eel.is/c++draft/dcl.attr.nodiscard
    accessed: 2026-10-06
    kind: spec
    version: "working draft"
    applicability: "States that discarding the result of a nodiscard call is discouraged and that implementations should issue a warning. This is recommended practice, not a compile error."
---

## Short answer

**Two-phase init: a simple constructor that cannot fail plus a separate `init()` method that returns an error code.** A constructor cannot return an error code and exceptions are off,[^cpp-draft-class-ctor-general] so everything that can fail moves into `err_t init()`, which the caller must check. The cost is that the object is not usable before `init()`,[^cppcg-c41] so the Core Guidelines prefer a factory function that returns the value together with an error.[^cppcg-c42][^cppcg-e27]

Rule: a simple (no-fail) constructor, fallible logic in a separate init with a return code, result always checked.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
