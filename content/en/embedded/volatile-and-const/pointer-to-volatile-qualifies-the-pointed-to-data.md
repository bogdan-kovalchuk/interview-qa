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

**`p` is a pointer to volatile `uint32_t`**.

The pointer `p` itself can be changed: it can point to a different address. But every `*p` must be a real volatile access to the object. This is the normal form for accessing a hardware register when the address may be chosen at runtime.

Reading rule: start from the name `p`: `p` is pointer to volatile `uint32_t`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
