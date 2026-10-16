---
id: emb-dtypes-0026
title: "Why can't you rely on `sizeof(int)` in network/serial protocols?"
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

`int` width depends on the C implementation and ABI, so its raw bytes do not define a portable message format.[^iso-c-n1570] Use `uint16_t` only when appropriate and available, then serialize it in a defined byte order; the type does not specify wire order.

If one side sends two bytes and the other reads four, fields shift or are misread. Define the format in the protocol, independent of either device's `int` width.[^iso-c-n1570]

## Detailed explanation

TODO
