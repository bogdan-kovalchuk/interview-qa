---
id: emb-patterns-0010
title: "How are full and empty distinguished in a ring buffer without a counter?"
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

**Empty: `head == tail`. Full: `((head + 1) & MASK) == tail`** (one slot is always left empty).

This avoids a shared `count` that both the ISR (interrupt service routine) and main update.

The cost is one less usable entry. This removes the shared `count` update, but does not by itself prove lock-free or race-free operation: atomicity and access ordering must be correct for the particular MCU and compiler.[^iso-c-n1570]

## Detailed explanation

TODO
