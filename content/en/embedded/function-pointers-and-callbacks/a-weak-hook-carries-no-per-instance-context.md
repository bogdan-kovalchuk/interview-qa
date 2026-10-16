---
id: emb-fnptr-0053
title: "Trap: why are weak hooks worse than an explicit callback for several driver instances?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-weak-attribute
    title: "GCC: Common Function Attributes – weak"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
---

## Short answer

<span class="warn">A weak hook does not carry per-instance context by itself.</span>[^gcc-weak-attribute]

If there are two UARTs or two timers, a function with one global name does not identify which instance owns the event. A weak override is also selected at link time rather than registered separately for each device.[^gcc-weak-attribute]

For reusable drivers, pass the callback and context separately; reserve weak hooks for global startup defaults or board-level extension points.

## Detailed explanation

TODO
