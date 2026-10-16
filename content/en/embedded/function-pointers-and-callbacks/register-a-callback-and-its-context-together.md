---
id: emb-fnptr-0006
title: "What does a typical embedded callback contract look like?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

The callback contract stores a function pointer and data pointer `context`, which the driver passes when an event occurs.

`typedef void (*uart_rx_cb_t)(void *ctx, uint8_t byte);` `int uart_set_rx_callback(Uart *u, uart_rx_cb_t cb, void *ctx);`

`void *` is for object addresses, not function addresses.[^iso-c-n1570] `ctx` must point to a live object of the expected type.

The API must define when and from which execution context the callback runs, along with its restrictions.

## Detailed explanation

TODO
