---
id: emb-macros-0031
title: "Trap: why can `inline` without `static` produce a linker error in C?"
description: "In C99+ a bare inline function provides only an inline definition and creates no external symbol for the linker."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
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

In C99+, a definition of a function with external linkage declared simply `inline` is an inline definition, not an external definition; by itself, it does not guarantee an external symbol for the linker.[^iso-c-n1570]

If a call needs an external definition but no translation unit provides one, the linker may report a missing symbol. The compiler is not required to inline the call.[^iso-c-n1570]

For a function defined in a header separately in each translation unit, a common choice is `static inline`, which gives it internal linkage in each translation unit.[^iso-c-n1570]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
