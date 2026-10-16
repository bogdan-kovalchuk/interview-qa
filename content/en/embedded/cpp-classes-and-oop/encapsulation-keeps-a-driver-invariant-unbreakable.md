---
id: emb-cppoop-0033
title: "What is encapsulation and which guarantee does it give in a driver?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-access-general
    title: "C++ working draft: Member access control, general ([class.access.general])"
    url: https://eel.is/c++draft/class.access.general
  - source_id: cpp-core-guidelines-c2
    title: "C++ Core Guidelines: C.2 (class or struct, invariant)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c2-use-class-if-the-class-has-an-invariant-use-struct-if-the-data-members-can-vary-independently
  - source_id: cpp-core-guidelines-c9
    title: "C++ Core Guidelines: C.9 (minimize exposure of members)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c9-minimize-exposure-of-members
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
---

## Short answer

**Hiding internal state behind a public interface** so that only the class's own operations maintain its invariant.

A driver keeps registers and buffers `private` and exposes only validated operations; code outside the class cannot name such members, so it cannot bypass the checks.[^cpp-draft-class-access-general] This is a language rule, not memory protection: `friend`, type casts or a direct write to an address bypass it.

Rule: it is a compile-time check, so it usually adds nothing at runtime; only the checks you write cost anything.

## Detailed explanation

TODO
