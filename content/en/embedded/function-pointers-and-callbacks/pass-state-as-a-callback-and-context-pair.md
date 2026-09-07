---
id: emb-fnptr-0030
title: "How do you pass state into a C callback without global variables?"
description: "Pass state through a callback plus context pointer pair."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: mechanism
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

Through a `callback + context pointer` pair.

Example: `timer_start(timer, on_timeout, &app);` – the driver stores `on_timeout` and `&app`. When the timer fires, it calls `on_timeout(&app)`. The callback casts `void *` back to `struct App *`.

Rule: a callback must not guess a global instance; a context pointer makes the dependency explicit.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
