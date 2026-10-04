---
id: emb-macros-0024
title: "How do you define an `ARRAY_SIZE` macro and where does it break dangerously?"
description: "Returns the number of array elements at compile time but breaks dangerously when passed a pointer."
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
---

## Question code

```c
#define ARRAY_SIZE(a) (sizeof(a) / sizeof((a)[0]))
```

## Short answer

Returns the number of elements in an array at compile time.

<span class="warn">Trap</span>: if you pass a pointer (including a function parameter array that decays to a pointer), `sizeof(a)` gives the pointer size, and the result is wrong.

Protection: apply only to real arrays in the same scope; GCC/Clang have a trick with `__builtin_types_compatible_p` that gives a compile error on a pointer; in C++ – `std::size`/template.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
