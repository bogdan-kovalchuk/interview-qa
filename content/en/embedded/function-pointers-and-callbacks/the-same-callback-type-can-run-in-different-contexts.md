---
id: emb-fnptr-0050
title: "Why must a callback API document its execution context?"
description: "The same callback type can be invoked from ISR, task, main loop or driver lock context."
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

**Because the same callback type can be invoked from ISR, task, main loop or driver lock context.**

This determines whether you can block, call malloc or printf, take a mutex, start DMA or call other driver APIs. Without documentation the caller can easily write a callback that works in a test but deadlocks in the real system.

Rule: in a callback contract always describe context, allowed operations, reentrancy, lifetime and ownership.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
