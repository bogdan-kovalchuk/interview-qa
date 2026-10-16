---
id: emb-patterns-0031
title: "Why is `volatile` not enough for a safe `count++` between an ISR and main?"
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

<span class="warn">`volatile` does not make `count++` atomic or synchronize an ISR with main.</span>

Increment is a read-modify-write: an interrupt between the read and write can lose an update. `volatile` affects accesses to volatile objects under the implementation's rules, but does not guarantee atomicity or inter-context ordering; ISR interaction rules depend on the implementation.[^iso-c-n1570]

Use a documented atomic type or a short critical section supported by the target platform; `volatile` alone is not enough.[^iso-c-n1570]

## Detailed explanation

TODO
