---
id: emb-structs-0039
title: "How do assignment and `memcpy` differ for structs?"
description: "Structure assignment copies the struct as a whole object; memcpy copies raw bytes including padding."
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

**Structure assignment copies the struct value as a whole object**; practically this may include padding bytes, but the semantics describe copying member values.

`memcpy` copies the raw object representation byte by byte. For trivially stored C structs both often give the same observable result for the fields, but `memcpy` may copy padding with undefined bytes.

Rule: for ordinary struct copying use assignment; for wire/storage serialization do not copy padding bytes unnecessarily.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
