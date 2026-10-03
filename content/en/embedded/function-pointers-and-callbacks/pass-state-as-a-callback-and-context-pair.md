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

Through a `callback + context pointer` pair.

Example: `timer_start(timer, on_timeout, &app);` – the driver stores the function pointer and the address of the state object. When the timer fires, it passes the saved context to the callback; the callback converts `void *` back to `struct App *` and accesses the object through the correct type. C allows an object pointer to be converted to `void *` and back while preserving the original value.[^iso-c-n1570]

Rule: a callback must not guess a global instance; a context pointer makes the dependency explicit.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
