---
id: emb-patterns-0005
title: "Trap: why must an FSM dispatcher take `state_t *state` rather than `state_t state`?"
description: "In C arguments are passed by value, so a local copy of state loses the transition on return."
track: embedded
section: common-code-patterns
level: junior
type: pitfall
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

<span class="warn">In C, arguments are passed by value</span> – modifying a local copy of `state` is lost on return, and the state transition is gone. FSM here stands for finite state machine.

```c
// баг: правиться лише копія
void process(state_t state, ...);
// fix: правиться справжній стан
void process(state_t *state, ...);
```

Especially easy to forget with `enum`, since it behaves like a plain int.

Mitigation: to let a function modify a variable that outlives the call, pass a pointer.[^embeddedinterviewlab]

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
