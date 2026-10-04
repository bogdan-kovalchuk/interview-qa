---
id: emb-macros-0030
title: "Why are `enum`/`const` often better than `#define` for named constants in C?"
description: "enum and const have type and scope visible to the debugger, unlike the typeless text substitution of #define."
track: embedded
section: inline-and-macros
level: junior
type: concept
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

## Short answer

**Enum enumerators and `const` objects are C declarations with a type and scope**, whereas `#define` substitutes preprocessing tokens and does not create a typed C identifier.[^iso-c-n1570]

`enum { MAX_CH = 8 };` provides an integer constant expression. A `const` object has a declared type, but in C it is not an integer constant expression for an ordinary array bound.[^iso-c-n1570]

Use `enum` for sets of integer constants, `const` for a typed object, and `#define` when you specifically need preprocessor behavior.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
