---
id: emb-structs-0044
title: "What is an anonymous struct/union and where does it appear?"
description: "Anonymous struct/union allows accessing nested members without an intermediate object name."
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

**An anonymous struct/union** allows accessing nested members without naming the intermediate object, provided the standard/compiler supports it in the relevant mode.

In embedded headers this is often used for register views: one register can be seen as a raw `uint32_t` or as a set of fields. This is convenient but may be compiler-specific in older C modes.

Rule: check whether anonymous union/struct are allowed by the standard and the project coding standard; for portable public headers, err on the side of caution.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
