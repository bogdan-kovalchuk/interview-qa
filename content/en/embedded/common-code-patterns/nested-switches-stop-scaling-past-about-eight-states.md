---
id: emb-patterns-0003
title: "Trap: when does an enum plus switch state machine become unwieldy?"
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

<span class="warn">When there are many transitions</span> nested `switch` statements can grow large and become hard to read and maintain.

Each new state requires editing a large `switch`, increasing the risk of missing a transition or case.

Mitigation: review the transition structure; a function-pointer table may help, but it still needs an entry when a state is added.[^iso-c-n1570]

## Detailed explanation

TODO
