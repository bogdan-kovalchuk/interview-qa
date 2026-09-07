---
id: emb-structs-0018
title: "Why is a discriminator tag often added to a `union`?"
description: "Because the union itself does not remember which member is currently active or logically valid."
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

**Because the union itself does not remember which member is currently active or logically valid.**

Typical pattern: `enum kind` alongside `union payload`. Without a discriminator, code can read a temperature payload as a pressure payload or interpret a pointer as an integer. This is a logical error even where binary access is formally possible.

Rule: for variant data, a struct must contain a tag plus a union, and all switches on the tag must handle every variant.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
