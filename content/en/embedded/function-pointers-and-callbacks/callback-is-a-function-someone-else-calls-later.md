---
id: emb-fnptr-0012
title: "What is a callback?"
description: "A callback is a function whose address is passed to other code to be called later on a certain event."
track: embedded
section: function-pointers-and-callbacks
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

**A callback** is a function whose address is passed to other code so that it can call it later upon a certain event or condition.

In C, a callback is most often implemented with a function pointer. For example, a UART driver calls a callback when a byte is received, a timer on timeout, a parser when it finds a frame, and `qsort` when it needs to compare two elements.

Interview rule: a function pointer is the mechanism; a callback is the role or usage pattern of that mechanism.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
