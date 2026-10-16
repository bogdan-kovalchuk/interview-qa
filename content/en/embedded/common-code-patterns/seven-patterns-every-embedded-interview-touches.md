---
id: emb-patterns-0001
title: "Which seven basic embedded C patterns are worth knowing for an interview?"
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

**State machines, ring buffers, bit manipulation, error handling, memory-mapped I/O, volatile-safe patterns, guard clauses.**

A good embedded version of these patterns is usually heap-free and has a clear answer to whether it is safe for ISR (interrupt service routine) / main loop interaction. Not every pattern is automatically ISR-safe – safety depends on shared state, atomicity and blocking calls.[^iso-c-n1570]

Rule: when asked “which patterns do you use”, name them with their trade-offs, not just a list.[^embeddedinterviewlab]

## Detailed explanation

TODO
