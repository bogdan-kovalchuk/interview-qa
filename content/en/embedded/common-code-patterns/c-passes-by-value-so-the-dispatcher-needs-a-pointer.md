---
id: emb-patterns-0005
title: "Trap: how can an FSM dispatcher preserve a state transition after it returns?"
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
