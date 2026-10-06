---
id: emb-cppoop-0033
title: "What is encapsulation and which guarantee does it give in a driver?"
description: "Hiding internal state behind a public interface so that only the class's own operations maintain its invariant"
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
  - source_id: cpp-draft-class-access-general
    title: "C++ working draft: Member access control, general ([class.access.general])"
    url: https://eel.is/c++draft/class.access.general
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that a private member can be named only by members and friends of the class, that access control concerns the ability to name a member, and that a construct using an inaccessible member is ill-formed. A language rule about names, not memory or hardware protection; says nothing about runtime cost."
  - source_id: cpp-core-guidelines-c2
    title: "C++ Core Guidelines: C.2 (class or struct, invariant)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c2-use-class-if-the-class-has-an-invariant-use-struct-if-the-data-members-can-vary-independently
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Rule C.2 and its note: an invariant is a logical condition on an object's members that a constructor must establish so that public functions can assume it; if the members vary independently, no invariant is possible. A style convention, not a language requirement."
  - source_id: cpp-core-guidelines-c9
    title: "C++ Core Guidelines: C.9 (minimize exposure of members)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c9-minimize-exposure-of-members
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Rule C.9: to enforce a relation (invariant) among members, make them private and maintain the relation through constructors and member functions; hiding reduces the chance of unintended access. A style recommendation, not a language requirement; says nothing about runtime cost."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Documents that without optimization GCC does not expand functions inline (-fno-inline is the default), that -finline-small-functions is enabled at -O2, -O3 and -Os, and that -flto allows inlining across object files; the actual heuristic decisions depend on the code."
---

## Short answer

**Hiding internal state behind a public interface** so that only the class's own operations maintain its invariant.

A driver keeps registers and buffers `private` and exposes only validated operations; code outside the class cannot name such members, so it cannot bypass the checks.[^cpp-draft-class-access-general] This is a language rule, not memory protection: `friend`, type casts or a direct write to an address bypass it.

Rule: it is a compile-time check, so it usually adds nothing at runtime; only the checks you write cost anything.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
