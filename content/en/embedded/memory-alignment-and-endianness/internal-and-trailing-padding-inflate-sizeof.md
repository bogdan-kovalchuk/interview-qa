---
id: emb-align-0028
title: "Trap: why is `sizeof(struct)` not the sum of its field sizes?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">Because of padding</span> between fields to meet their alignment and at the end to preserve struct alignment in arrays. Exact layout depends on the ABI and implementation.

For an ABI with alignments of 1, 4, and 2 bytes, `{uint8_t; uint32_t; uint16_t;}` uses 1 + 3 padding + 4 + 2 + 2 trailing padding = 12 bytes, not 7.[^iso-c-n1570]

Guard: for layout analysis always use `sizeof` and `offsetof`; do not sum fields in your head.[^embeddedinterviewlab]

## Detailed explanation

TODO
