---
id: emb-patterns-0013
title: "Why are the fields of a ring buffer struct marked `volatile`?"
description: "head and tail are modified in one context and read in another, so volatile prevents the compiler from caching them."
track: embedded
section: common-code-patterns
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

**On many MCUs, `volatile` is used for indexes modified by an ISR and read by main, but it is not a portable synchronization guarantee.**

Without an appropriate mechanism, the compiler may reuse an earlier index value. `volatile` requires accesses to volatile objects under the implementation's rules, but does not by itself guarantee atomicity or cross-context ordering for the data buffer.

Check the compiler and MCU documentation for ISR behavior, index atomicity, and barriers; use a supported atomic mechanism or critical section when stronger synchronization is needed.[^iso-c-n1570]
## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
