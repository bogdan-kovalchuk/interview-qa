---
id: emb-structs-0021
title: "What is the range of `unsigned mode : 3`?"
description: "From 0 to 7; three unsigned bits represent 2^3 = 8 values."
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

**From `0` to `7`**.

Three unsigned bits represent `2^3 = 8` values. Writing a value outside the range into an unsigned bit-field is usually truncated modulo `2^width`, but this should not be relied on as validation logic.

Embedded rule: before writing to a bit-field or register field, mask and check the value explicitly, especially if the source comes from protocol/input.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
