---
id: emb-structs-0052
title: "Why is `sizeof(struct with flexible array)` not the full packet size?"
description: "The flexible array member has no compile-time size and is not included in sizeof."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: mechanism
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

**Because a flexible array member has no fixed length and contributes no elements to the structure's `sizeof`.**

`sizeof(struct Packet)` returns the structure size, including possible padding, but not any `data[]` elements. The real size is `sizeof(struct Packet) + payload_len * sizeof data[0]`.

Rule: a flexible array member describes the prefix layout, it does not own storage automatically.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
