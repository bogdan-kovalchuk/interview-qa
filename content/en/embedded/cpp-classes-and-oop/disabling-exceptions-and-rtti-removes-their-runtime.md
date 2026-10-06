---
id: emb-cppoop-0025
title: "Why are `-fno-exceptions` and `-fno-rtti` used in embedded C++?"
description: "-fno-exceptions omits the code and data for propagating exceptions, -fno-rtti the type information for dynamic_cast and typeid; the price is no throw and no downcasts."
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
  - source_id: gcc-fexceptions
    title: "GCC: Options for Code Generation Conventions (-fexceptions)"
    url: https://gcc.gnu.org/onlinedocs/gcc/Code-Gen-Options.html#index-fexceptions
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "Documents -fexceptions: extra code to propagate exceptions and, for some targets, unwind information for all functions, which can add significant data size overhead although it does not affect execution; GCC enables it by default for C++. GCC-specific; there is no separate entry for -fno-exceptions, and it does not say how the compiler rejects throw."
  - source_id: gcc-fno-rtti
    title: "GCC: C++ Dialect Options (-fno-rtti)"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html#index-fno-rtti
    accessed: 2026-10-06
    kind: official
    version: "current"
    applicability: "Documents -fno-rtti: disables generating information about classes with virtual functions for dynamic_cast and typeid, which saves space; G++ generates the information for exceptions as needed; dynamic_cast stays usable for casts that need no RTTI (to void* or to an unambiguous base); mixing -frtti and -fno-rtti may not work. GCC-specific."
  - source_id: iso-tr-18015
    title: "ISO/IEC TR 18015:2006 Technical Report on C++ Performance"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/TR18015.pdf
    accessed: 2026-10-06
    kind: spec
    version: "TR 18015:2006"
    applicability: "Section 5.4.2.1 says the time from throw to catch is hard to predict (destroying automatic objects, consulting tables), so current implementations may be unsuitable for some applications, while with a statically known call tree it can in principle be analysed. Section 5.4.1.2 describes the table model: no run-time overhead unless something is thrown, but the static tables can be large, which matters on some embedded systems. Section 5.3.1 puts type information at about 40 bytes per class. A 2006 report: figures depend on the implementation."
---

## Short answer

**`-fno-exceptions` omits the code and data needed to propagate exceptions, and `-fno-rtti` omits the type information for `dynamic_cast` and `typeid`.**[^gcc-fexceptions][^gcc-fno-rtti] This shrinks the binary, and the time from `throw` to `catch` is hard to predict, so exceptions may not suit real-time work.[^iso-tr-18015] So on such targets do not use `throw`, `typeid` or a downcasting `dynamic_cast` – rely on error codes and static polymorphism.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
