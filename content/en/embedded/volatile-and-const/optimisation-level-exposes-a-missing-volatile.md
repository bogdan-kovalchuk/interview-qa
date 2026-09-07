---
id: emb-volconst-0048
title: "Trap: why does \"works in debug, breaks in release\" often point at a missing `volatile`?"
description: "A debug build typically uses -O0, while a release build enables optimizations."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
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

<span class="warn">Because a debug build typically uses `-O0`, while a release build enables optimizations.</span>

At `-O0`, the compiler often performs every read literally, so a missing `volatile` can go unnoticed. At `-O2`, it caches values, removes redundant reads and writes, and exposes the false assumption that hardware memory behaves like ordinary RAM.

Protection: if peripheral polling or a sensor read returns stale data only in release, check register pointer types and volatile qualifiers first.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
