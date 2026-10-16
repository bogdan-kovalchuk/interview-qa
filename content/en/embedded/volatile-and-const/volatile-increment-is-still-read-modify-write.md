---
id: emb-volconst-0053
title: "Why is `volatile uint32_t counter; counter++;` unsafe for an ISR-shared counter?"
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

<span class="warn">`counter++` reads, computes, and writes; `volatile` does not make that sequence atomic.</span>[^iso-c-n1570]

The expression `counter++` must read the value, compute a new one, and write it. If an interrupt can occur between these steps and modify the same counter, an update can be lost. The exact access rules for an ISR-shared object depend on the implementation and platform.[^iso-c-n1570]

Defense: use a critical section that covers both contexts, or an atomic operation supported by the platform.[^iso-c-n1570]

## Detailed explanation

TODO
