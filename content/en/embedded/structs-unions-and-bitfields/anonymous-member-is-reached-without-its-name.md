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

**An anonymous struct/union** lets code access its members without naming an intermediate object; in C11 this is a standard rule for an unnamed member whose type is an anonymous `struct` or `union`.[^iso-c-n1570]

Embedded headers can use this for register views, though support depends on the compiler mode.

Check the language mode and compiler documentation: older modes or extensions can differ. In a public header, all translation units must also see a consistent declaration so that layout and available names agree.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
