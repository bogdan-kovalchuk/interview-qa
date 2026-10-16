---
id: emb-patterns-0002
title: "What does a state machine built on `enum` plus `switch` look like?"
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
oven_state_t step(oven_state_t s, oven_event_t e) {
  switch (s) {
  case STATE_IDLE:
    if (e == EVT_START) return STATE_HEATING;
    break;
  // ... інші стани
  }
  return s; // no transition
}
```

## Short answer

**Nested `switch` on state, inside – event check and return of the new state.**

Advantages: easy to step through in a debugger, and checking all `enum` cases can reveal a missing transition. If there is no transition – return the current state.[^iso-c-n1570]

Rule: enum+switch is the best choice for small FSMs.[^embeddedinterviewlab]

## Detailed explanation

TODO
