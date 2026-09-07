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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**`enum` and `const` have a type and scope, visible to the debugger**, whereas `#define` is a typeless text substitution with no scope.

`enum { MAX_CH = 8 };` gives a compile-time integer constant with a name in the debug info and does not pollute the global namespace. `const` is also type-safe, but in C it occupies memory and is not an integer constant expression for array size.

Rule: integer compile-time constants -> `enum`; typed constants -> `const`; `#define` when you specifically need the preprocessor.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
