---
id: emb-patterns-0002
title: "What does a state machine built on `enum` plus `switch` look like?"
description: "Nested switch on state with an inner event check and return of the new state."
track: embedded
section: common-code-patterns
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

Advantages: easy to step through in a debugger, the compiler warns about missed `enum` cases. If there is no transition – return the current state.

Rule: enum+switch is the best choice for small FSMs.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
