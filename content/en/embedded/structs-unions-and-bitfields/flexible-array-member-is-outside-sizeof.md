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

**Because the flexible array member has no compile-time size and is not included in `sizeof`.**

`sizeof(struct Packet)` returns only the header size up to the payload, possibly with padding before `data[]`. The real packet size must be calculated as `sizeof(struct Packet) + payload_len`.

Rule: a flexible array member describes the prefix layout, it does not own storage automatically.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
