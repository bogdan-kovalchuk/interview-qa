---
id: emb-dtypes-0037
title: "What is the difference between `uint32_t` and `unsigned int` for portability?"
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

`unsigned int` is at least 16 bits, and its width depends on the implementation; the C standard does not tie it to an MCU name.[^iso-c-n1570] `uint32_t` is available only when an implementation has an unsigned integer type exactly 32 bits wide with no padding bits, and then it has that width.[^iso-c-n1570] Use an exact-width type for protocol fields and registers when available and required by the specification; use `size_t` for object sizes.

## Detailed explanation

TODO
