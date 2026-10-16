---
id: emb-volconst-0035
title: "Does reading a volatile object count as a side effect?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**An access through a `volatile` lvalue is a side effect and must be evaluated according to the C abstract machine.**[^iso-c-n1570]

Therefore, the compiler cannot simply discard a volatile hardware-register read as an "unused result." The read may clear a flag, acknowledge an interrupt, or trigger a bus transaction; the implementation defines what counts as an access.

Embedded rule: if a read-to-clear or read-has-side-effect register is described without `volatile`, the optimizer can break the peripheral protocol. `volatile` does not provide atomicity, inter-thread synchronization, or a universal memory barrier.[^iso-c-n1570]

## Detailed explanation

TODO
