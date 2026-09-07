---
id: emb-structs-0048
title: "What is the common initial sequence in a union of structs?"
description: "C allows inspecting the common initial part of structs in a union under certain conditions."
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

**C allows inspecting the common initial part of structs in a union under certain conditions**, when the structs share compatible initial members.

This pattern is used for tagged variants, where the first field is a tag/type shared by all variants. But this is a subtle part of the standard, and it is easy to port incorrectly to C++ or break with a layout change.

Rule: for simplicity and portability, it is often better to place the tag outside the union than to rely on the common initial sequence.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
