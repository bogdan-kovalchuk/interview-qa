---
id: emb-volconst-0009
title: "What does the declaration `volatile uint32_t *p` mean?"
description: "p is a pointer to volatile uint32t; the pointer itself can be reassigned, but every dereference is a real volatile access."
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

**`p` is a pointer to volatile `uint32_t`**.

The pointer `p` itself can be changed: it can point to a different address. But every `*p` must be a real volatile access to the object. This is the normal form for accessing a hardware register when the address may be chosen at runtime.

Reading rule: start from the name `p`: `p` is pointer to volatile `uint32_t`.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
