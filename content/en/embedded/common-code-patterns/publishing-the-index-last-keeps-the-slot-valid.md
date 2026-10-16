---
id: emb-patterns-0035
title: "Why does the ISR write the slot before advancing `head`?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: linux-circular-buffers
    title: "Circular Buffers (The Linux Kernel documentation)"
    url: https://www.kernel.org/doc/html/latest/core-api/circular-buffers.html
  - source_id: gcc-volatiles
    title: "GCC 16.1.0: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Volatiles.html
---

## Short answer

**To ensure the consumer never sees an advanced `head` pointing at a byte not yet written.**

`head` publishes the record: the consumer treats every slot before it as ready, so the data must be written and visible first. This matters when the consumer can run "in the middle" (another core, a nested interrupt, a preempted task) and against compiler or CPU reordering – so publish `head` with a release store and read it with an acquire load.[^linux-circular-buffers][^iso-c-n1570]

Rule: producer: data -> `head`; consumer: data -> `tail`.

## Detailed explanation

TODO
