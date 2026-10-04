---
id: emb-patterns-0004
title: "What does a state machine built on a function-pointer table look like?"
description: "Array of function pointers indexed by state with a single O(1) lookup for dispatch."
track: embedded
section: common-code-patterns
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

## Sources

<!-- generated from frontmatter -->
