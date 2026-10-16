---
id: emb-cppoop-0011
title: "How do you initialise an object when exceptions are disabled (`-fno-exceptions`)?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-ctor-general
    title: "C++ working draft: Constructors ([class.ctor.general])"
    url: https://eel.is/c++draft/class.ctor.general
  - source_id: cppcg-c41
    title: "C++ Core Guidelines: C.41 – A constructor should create a fully initialized object"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c41-a-constructor-should-create-a-fully-initialized-object
  - source_id: cppcg-c42
    title: "C++ Core Guidelines: C.42 – If a constructor cannot construct a valid object, throw an exception"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c42-if-a-constructor-cannot-construct-a-valid-object-throw-an-exception
  - source_id: cppcg-c44
    title: "C++ Core Guidelines: C.44 – Prefer default constructors to be simple and non-throwing"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c44-prefer-default-constructors-to-be-simple-and-non-throwing
  - source_id: cppcg-e27
    title: "C++ Core Guidelines: E.27 – If you can't throw exceptions, use error codes systematically"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#e27-if-you-cant-throw-exceptions-use-error-codes-systematically
  - source_id: cpp-draft-dcl-attr-nodiscard
    title: "C++ working draft: Nodiscard attribute ([dcl.attr.nodiscard])"
    url: https://eel.is/c++draft/dcl.attr.nodiscard
---

## Short answer

**Two-phase init: a simple constructor that cannot fail plus a separate `init()` method that returns an error code.** A constructor cannot return an error code and exceptions are off,[^cpp-draft-class-ctor-general] so everything that can fail moves into `err_t init()`, which the caller must check. The cost is that the object is not usable before `init()`,[^cppcg-c41] so the Core Guidelines prefer a factory function that returns the value together with an error.[^cppcg-c42][^cppcg-e27]

Rule: a simple (no-fail) constructor, fallible logic in a separate init with a return code, result always checked.

## Detailed explanation

TODO
