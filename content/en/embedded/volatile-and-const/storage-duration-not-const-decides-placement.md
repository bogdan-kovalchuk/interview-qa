---
id: emb-volconst-0027
title: "Trap: does a local `const` array always live in Flash?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: avr-libc-program-space
    title: "AVR-LibC: Data in Program Space"
    url: https://avrdudes.github.io/avr-libc/avr-libc-user-manual/pgmspace.html
---

## Short answer

<span class="warn">No, not always.</span>

`const` forbids modification through that identifier, but does not determine physical placement. A local automatic `const` object may require stack storage or be optimized away; file-scope or `static const` objects commonly go into a read-only section, but not necessarily Flash.

For a large immutable LUT, use `static const` or file-scope `const`, then check the map file for its actual placement.[^avr-libc-program-space]

## Detailed explanation

TODO
