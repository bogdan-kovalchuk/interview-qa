---
id: emb-dtypes-0053
title: "What is the bug here? `char buf[256]; buf[256] = '\\0';`"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

For `char buf[256]`, valid indices are `0..255`; `buf[256]` does not designate an array element, and writing there has undefined behavior.[^iso-c-n1570]

The standard does not define the outcome: data may be corrupted or the program may fail, but no particular variable or address can be predicted.[^iso-c-n1570]

To store 256 characters plus the terminating `\\0`, the buffer needs at least 257 bytes; for a shorter string, write the terminator within the actual capacity.[^iso-c-n1570]

## Detailed explanation

TODO
