---
id: emb-patterns-0004
title: "What does a state machine built on a function-pointer table look like?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Question code

```c
typedef void (*handler_t)(oven_event_t e);
static const handler_t handlers[] = {
  [STATE_IDLE]    = on_idle,
  [STATE_HEATING] = on_heating,
  [STATE_ERROR]   = on_error,
};
handlers[*state](evt);
```

## Short answer

**An array of handler pointers can select a function by state index in one lookup.**

Advantages: a separate function per state isolates the logic. An initialized `static const` table is usually placed in a read-only section, but the physical segment depends on the toolchain and linker script.[^iso-c-n1570]

Rule: scalable for many states, but harder to read in a debugger.[^embeddedinterviewlab]

## Detailed explanation

TODO
