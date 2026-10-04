---
id: emb-patterns-0005
title: "Trap: how can an FSM dispatcher preserve a state transition after it returns?"
description: "In C a parameter receives a copy of the value; pass an address or return a new value to change the caller's state."
track: embedded
section: common-code-patterns
level: junior
type: pitfall
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

<span class="warn">A C function parameter receives its own argument value</span> – changing local `state` does not change the caller's variable. FSM means finite state machine.[^iso-c-n1570]

```c
// баг: правиться лише копія
void process(state_t state, ...);
// fix: правиться справжній стан
void process(state_t *state, ...);
```

Using an `enum` does not change the argument-passing rule.

To let the dispatcher modify the caller's state, pass its address and write through the pointer; check for `NULL` when the function contract permits it.[^iso-c-n1570]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
