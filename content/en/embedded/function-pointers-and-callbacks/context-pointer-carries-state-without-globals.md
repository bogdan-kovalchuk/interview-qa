---
id: emb-fnptr-0005
title: "Why do callback APIs often carry a `void *context` parameter?"
description: "context passes the callback user state without global variables."
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

**`context` passes the callback user state without global variables.**

A callback function by itself carries no captured state, unlike a lambda with capture in C++. Therefore the driver stores a pair: function pointer + context pointer. When the event occurs, the driver calls `cb(context)`, and the callback casts context to its own type.

Rule: a callback without context quickly forces the use of globals; a callback with context scales to multiple UART/SPI/timer instances.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
