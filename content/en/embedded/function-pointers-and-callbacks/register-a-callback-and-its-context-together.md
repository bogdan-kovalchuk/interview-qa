---
id: emb-fnptr-0006
title: "What does a typical embedded callback contract look like?"
description: "A typical contract registers a function pointer and context, and the driver calls them on the event."
track: embedded
section: function-pointers-and-callbacks
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

The callback contract stores a function pointer and data pointer `context`, which the driver passes when an event occurs.

`typedef void (*uart_rx_cb_t)(void *ctx, uint8_t byte);` `int uart_set_rx_callback(Uart *u, uart_rx_cb_t cb, void *ctx);`

`void *` is for object addresses, not function addresses.[^iso-c-n1570] `ctx` must point to a live object of the expected type.

The API must define when and from which execution context the callback runs, along with its restrictions.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
