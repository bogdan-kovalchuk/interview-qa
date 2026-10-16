---
id: emb-fnptr-0041
title: "How do you make a C callback for a C++ object?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cppreference-member-pointers
    title: "cppreference: Pointers"
    url: https://en.cppreference.com/w/cpp/language/pointer
---

## Short answer

Use a static thunk plus a context pointer.

`static void thunk(void *ctx, uint8_t b) { static_cast<App *>(ctx)->on_rx(b); }` `uart_register(thunk, this);`

A static member function has no hidden `this` and is compatible with a plain function pointer if the signature matches. `ctx` restores the object instance manually.

Rule: this is the standard bridge between a C HAL and C++ class design.[^cppreference-member-pointers]

## Detailed explanation

TODO
