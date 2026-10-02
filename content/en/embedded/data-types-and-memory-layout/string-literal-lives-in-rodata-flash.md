---
id: emb-dtypes-0035
title: "Where does the string literal `\"Hello, World!\"` live in an embedded program's memory?"
description: "String literals often use a read-only section mapped to Flash, but placement depends on the toolchain and linker script."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
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
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

In a typical embedded build, a string literal often resides in a read-only section such as `.rodata` mapped to Flash, but this depends on the toolchain and linker script rather than being guaranteed by C.

The same string is used only once (deduplication is compiler-dependent).

<span class="warn">Separate object</span>: `char arr[] = "hello";` creates a modifiable array containing a copy of the characters; an automatic local array is usually on the stack, while a static array is in writable static storage. Check the target build's map file.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
