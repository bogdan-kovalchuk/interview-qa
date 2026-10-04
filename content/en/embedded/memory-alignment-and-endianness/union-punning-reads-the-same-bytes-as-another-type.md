---
id: emb-align-0039
title: "What is type punning through a union and what makes it risky?"
description: "Viewing the same bytes as a different type, risky because it depends on representation and may be undefined behavior."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 4
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
  - source_id: cpp-draft-class-union
    title: "C++ Working Draft: Unions"
    url: https://eel.is/c%2B%2Bdraft/class.union
    accessed: 2026-10-04
    kind: spec
    version: null
    applicability: "Describes active union members in C++; this rule should not be applied to C."
---

## Question code

```c
union { float f; uint32_t u; } x;
x.f = 1.5f;
// читаємо x.u - бітовий патерн float
```

## Short answer

**Viewing the same bytes as a different type.** In C, reading another union member interprets the stored representation as that member's type, but the result can be implementation-dependent; in C++, this read for these types generally has undefined behavior, so prefer `memcpy` or `std::bit_cast`.

The result depends on endianness and representation (for example IEEE 754), so for local inspection it can be useful but not for portable serialization.

Rule: for the wire do not use union layout; serialize explicitly with a known byte order.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
