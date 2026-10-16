---
id: emb-dtypes-0009
title: "Why use `stdint.h` types instead of plain `int`, `short`, `long`?"
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

The sizes and ranges of `int`, `short`, and `long` are specified by the C implementation, so they should not be assumed to match across ABIs. The `<stdint.h>` types `uintN_t`, when provided, have exactly N bits and no padding bits; these exact-width typedefs are optional if the implementation lacks a matching type. For protocols and bit fields, choose a type for the required width and specify representation and byte order separately.[^iso-c-n1570]

## Detailed explanation

TODO
