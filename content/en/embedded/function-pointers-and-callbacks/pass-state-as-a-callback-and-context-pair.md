---
id: emb-fnptr-0030
title: "How do you pass state into a C callback without global variables?"
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

Through a `callback + context pointer` pair.

Example: `timer_start(timer, on_timeout, &app);` – the driver stores the function pointer and the address of the state object. When the timer fires, it passes the saved context to the callback; the callback converts `void *` back to `struct App *` and accesses the object through the correct type. C allows an object pointer to be converted to `void *` and back while preserving the original value.[^iso-c-n1570]

Rule: a callback must not guess a global instance; a context pointer makes the dependency explicit.[^iso-c-n1570]

## Detailed explanation

TODO
