---
id: emb-volconst-0048
title: "Trap: why does \"works in debug, breaks in release\" often point at a missing `volatile`?"
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

<span class="warn">A debug/release difference can expose missing `volatile`, but the configuration name alone proves nothing.</span>

Different optimization flags can change generated code, and a register access without `volatile` may not be reread as the program expects. However, `-O0` does not guarantee the required ordering, and `-O2` does not necessarily cache every value; behaviour depends on the code and compiler.[^iso-c-n1570]

If peripheral polling returns stale data, check register pointer types and MCU access requirements; `volatile` is needed for applicable memory-mapped registers, but does not solve every concurrency or ordering problem.[^iso-c-n1570]

## Detailed explanation

TODO
