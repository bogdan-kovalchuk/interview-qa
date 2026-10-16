---
id: emb-patterns-0011
title: "Trap: why does a `count` field in a ring buffer create a race condition?"
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

<span class="warn">The ISR (interrupt service routine) increments `count` while main decrements it; these operations can conflict.</span>

`count++` and `count--` are read, compute, and write sequences, not guaranteed atomic operations; an interrupt can occur between those steps and overwrite an update.

The result is incorrect capacity accounting: the buffer may appear full or empty incorrectly. Use a critical section, a suitable atomic mechanism, or a design without a shared `count`.[^iso-c-n1570]

## Detailed explanation

TODO
