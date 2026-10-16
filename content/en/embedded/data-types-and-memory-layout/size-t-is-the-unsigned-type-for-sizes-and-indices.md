---
id: emb-dtypes-0087
title: "What is `size_t`, and why is it better than `int` for sizes and indices?"
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

**`size_t`** is an implementation-defined unsigned integer type large enough to represent the size of any object supported by the implementation; it is not necessarily `uint32_t` or `uint64_t`. `sizeof` produces `size_t`, as do `strlen` and `malloc` in their standard library declarations. Use a matching type for lengths and indices, while remembering that unsigned values cannot be negative and comparisons with `int` can trigger conversions.[^iso-c-n1570]

## Detailed explanation

TODO
