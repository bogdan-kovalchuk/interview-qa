---
id: emb-patterns-0038
title: "Why is an FSM function-pointer table made `static const`?"
description: "static const puts the table in Flash/.rodata, saving RAM and protecting the mapping from accidental overwrite."
track: embedded
section: common-code-patterns
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

**`static const` places the table in Flash/`.rodata`** – saves RAM and protects the mapping from accidental runtime overwrite.

If FSM (finite state machine) transitions do not change after build, a mutable global array is an unnecessary risk (corruption would redirect a call to a random address).

Rule: immutable dispatch/handler tables are always `static const`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
