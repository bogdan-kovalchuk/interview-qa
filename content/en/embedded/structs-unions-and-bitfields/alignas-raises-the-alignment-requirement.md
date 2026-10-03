---
id: emb-structs-0042
title: "What does `alignas`/`_Alignas` or a compiler-specific alignment attribute do?"
description: "Sets or strengthens the alignment requirement of a declared object."
track: embedded
section: structs-unions-and-bitfields
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
  - source_id: cpp-draft-dcl-align
    title: "C++ working draft: Alignment specifier [dcl.align]"
    url: https://eel.is/c++draft/dcl.align
    accessed: 2026-10-04
    kind: spec
    version: "Current working draft"
    applicability: "C++ rules for applying alignas to a variable, class data member, and class declaration; does not cover compiler-specific attributes."
---

## Short answer

**Sets or strengthens the alignment requirement of a declared object**; applying it to a type itself depends on the language or a compiler-specific extension.

In embedded, this is needed for DMA buffers, cache line alignment, vector tables, or peripheral requirements. For example, a DMA descriptor may require 16-byte alignment; cache maintenance on Cortex-M7 often operates on cache lines.

Rule: alignment is part of the hardware contract. Check the address at runtime or compile time and describe the requirement in the declaration, attribute, or linker script.[^iso-c-n1570] [^cpp-draft-dcl-align]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
