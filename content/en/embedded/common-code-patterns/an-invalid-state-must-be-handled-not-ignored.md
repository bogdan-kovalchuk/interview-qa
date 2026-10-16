---
id: emb-patterns-0006
title: "Why must a state machine handle the default or invalid state?"
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

**An unexpected state or event should be handled explicitly, not silently skipped.**

Corrupted data or external input can produce a value outside the valid state set. A missing `default` is not itself necessarily undefined behavior, but indexing a table without checking bounds can cause an out-of-bounds access.[^iso-c-n1570]

Add a `default`/error handler and check bounds before accessing the transition table.[^iso-c-n1570]

## Detailed explanation

TODO
