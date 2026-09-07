---
id: emb-structs-0050
title: "What does `typedef struct Foo Foo;` mean?"
description: "It creates a typedef name for struct Foo, often before the struct is fully defined."
track: embedded
section: structs-unions-and-bitfields
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

**It creates a typedef name `Foo` for the type `struct Foo`**, often before the struct is fully defined.

If the struct body is not given, `Foo` is an incomplete type. You can use `Foo *` in an API, but you cannot create a `Foo` object by value until the full definition.

Embedded use case: opaque handles for drivers: `Foo_Init(Foo *self)` or `Foo *Foo_Open(...)`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
