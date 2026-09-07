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

Typical contract: register a function pointer and context, and the driver calls them on the event.

`typedef void (*uart_rx_cb_t)(void *ctx, uint8_t byte);` `int uart_set_rx_callback(Uart *u, uart_rx_cb_t cb, void *ctx);`

The driver does not know the type of context. It only stores `ctx` and passes it back to the callback. This allows one callback code to work with different objects or buffers.

Rule: the API must document when the callback is called, from which context, whether blocking code may be called, and how long `ctx` lives.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
