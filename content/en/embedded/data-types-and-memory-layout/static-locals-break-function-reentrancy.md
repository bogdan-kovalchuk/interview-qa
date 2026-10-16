---
id: emb-dtypes-0057
title: "What is a reentrant function, and why do `static` locals break reentrancy?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: strtok-r-manpages
    title: "strtok_r(3) Linux man-pages"
    url: https://manpages.debian.org/testing/manpages-dev/strtok_r.3.en.html
---

## Short answer

**A reentrant function** can be called again before an earlier call finishes if each call has independent state or shared state is properly protected. A `static` local is shared across calls, but its presence alone does not make a function unsafe; conflicting access to mutable state is the issue.[^iso-c-n1570]

If an ISR reenters the function, both invocations may use the same static value. `strtok()` retains state between calls; POSIX `strtok_r()` takes a separate `saveptr`.[^iso-c-n1570][^strtok-r-manpages]

## Detailed explanation

TODO
