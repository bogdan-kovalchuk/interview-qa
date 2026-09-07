---
id: emb-fnptr-0013
title: "How does a function pointer differ from a callback?"
description: "A function pointer is a type or value; a callback is an architectural pattern."
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

**A function pointer is a type/value; a callback is an architectural pattern.**

A function pointer can sit in a command table, vector table, or vtable-like struct. A callback is when one module registers a function and another module calls it later, usually in response to an event.

Embedded example: `void (*isr)(void)` in a vector table is a function pointer; a user hook `on_rx(ctx, byte)` called by the UART driver is a callback.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
