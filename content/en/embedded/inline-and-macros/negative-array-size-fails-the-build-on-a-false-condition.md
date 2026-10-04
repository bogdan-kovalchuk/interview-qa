---
id: emb-macros-0033
title: "How do you do a compile-time check without `static_assert` in older C?"
description: "When a constant condition is false, the array bound becomes -1 and violates a language constraint, so the compiler diagnoses it during translation."
track: embedded
section: inline-and-macros
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: iso-c-array-static-assert
    title: "ISO/IEC 9899:201x Committee Draft N1570, array declarators and static assertions"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-10-04
    kind: spec
    version: N1570
    applicability: "C array bounds, integer constant expressions, constraint diagnostics, and _Static_assert in C11; it does not prescribe that every compiler abort after a diagnostic."
---

## Question code

```c
#define STATIC_ASSERT(c, name) \
  typedef char name[(c) ? 1 : -1]
```

## Short answer

**The negative array size trick**: if a constant condition is false, the bound becomes `-1` and violates a language constraint, so the compiler must diagnose it but may continue.[^iso-c-array-static-assert]

This is an old way to check a type property at compile time, such as a structure size, when the condition is constant: `STATIC_ASSERT(sizeof(Frame) == 8, frame_size)`.[^iso-c-array-static-assert]

Since C11 and C++11, `_Static_assert` and `static_assert` respectively provide a diagnostic message.[^iso-c-array-static-assert]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
