---
id: emb-dtypes-0024
title: "What is padding in structs, and where does it come from?"
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

Padding is space an implementation may insert between or after struct members to satisfy alignment requirements. For an ABI where `char` has size 1 and `int` requires four-byte alignment, `struct { char c; int x; }` places `x` at offset 4, with three bytes between the members. Exact offsets and total size depend on the implementation and ABI; they are not universal C guarantees.[^iso-c-n1570][^embeddedinterviewlab]

## Detailed explanation

TODO
