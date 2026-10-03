---
id: emb-volconst-0049
title: "Why is `const` not a guarantee that an object never physically changes?"
description: "const restricts writes through a specific typed access but does not prove that physical memory will never change."
track: embedded
section: volatile-and-const
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

**`const` restricts writes through a specific typed access, but it does not prove that the physical memory will never change.**

An object can be mutable yet passed into a function as `const T *` so that the function does not modify it. And `volatile const` directly describes a case where firmware does not write, but hardware can change the value.

Rule: `const` is a restriction on typed access in C; actual memory permissions depend on the device and its configuration.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
