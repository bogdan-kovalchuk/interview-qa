---
id: emb-fnptr-0001
title: "What is a function pointer in C?"
description: "A function pointer can be used to call a function of a compatible type indirectly."
track: embedded
section: function-pointers-and-callbacks
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

**A function pointer** designates a function of a particular type for indirect calls. The function type specifies its return type and parameters; C does not require an ordinary numeric code address.[^iso-c-n1570]

Unlike an object pointer, a function pointer has a pointer-to-function type, not a pointer-to-object type. Code can select a function and call it through the pointer; its representation is implementation-defined.[^iso-c-n1570]

Rule: the function type must be compatible with the call; similar declarations alone do not prove this.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
