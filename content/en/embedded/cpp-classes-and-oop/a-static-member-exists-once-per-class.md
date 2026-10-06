---
id: emb-cppoop-0028
title: "What is a static class member and where does it live?"
description: "A static data member is shared by all instances and lives in static storage rather than in each object"
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
  - source_id: cpp-draft-class-static
    title: "C++ working draft: Static members ([class.static])"
    url: https://eel.is/c++draft/class.static
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that a static data member is not part of the subobjects of a class, that there is one copy shared by all objects (one per thread for thread_local), that the in-class declaration of a non-inline static data member is not a definition, and that an inline static member is a definition. Does not specify placement in memory sections."
  - source_id: cpp-draft-basic-stc-static
    title: "C++ working draft: Static storage duration ([basic.stc.static])"
    url: https://eel.is/c++draft/basic.stc.static
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that variables first declared with static (and not thread-local) have static storage duration, i.e. their storage lasts for the whole program. Says nothing about .data or .bss sections."
  - source_id: cpp-draft-dcl-inline-variable
    title: "C++ working draft: The inline specifier ([dcl.inline])"
    url: https://eel.is/c++draft/dcl.inline
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that an inline variable with external linkage can be defined in multiple translation units and is one entity with one address. Does not concern placement in sections."
  - source_id: gcc-zero-bss
    title: "GCC 16.1.0: Optimize Options – -fno-zero-initialized-in-bss"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Documents GCC's default placement of zero-initialized globals in BSS and the option that changes it; does not describe every compiler or linker."
---

## Question code

```cpp
class Counter {
  static uint32_t count_; // одна на клас
};
```

## Short answer

**A static data member belongs to the class, not to an object:** one copy is shared by all instances (one per thread for `thread_local`), and it is not part of the class's subobjects, so it does not increase `sizeof`.[^cpp-draft-class-static] It has static storage duration,[^cpp-draft-basic-stc-static] so with GCC it lives outside the object: in `.bss` for a zero initial value, otherwise in the data section.[^gcc-zero-bss] A non-inline static member is defined once outside the class; `inline static` is a definition in the class itself.[^cpp-draft-class-static]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
