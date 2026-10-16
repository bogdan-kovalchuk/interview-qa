---
id: emb-dtypes-0084
title: "Why is it recommended to order struct fields from largest to smallest?"
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

Ordering fields by decreasing alignment often reduces struct padding, but exact size depends on the compiler ABI and target.[^iso-c-n1570]

With an ABI where `char` has size and alignment 1 and `int` has size and alignment 4, the first order occupies 12 bytes and the second 8.

Do not assume these alignment values on every MCU; verify the layout and `sizeof()` for the target ABI.[^iso-c-n1570]

## Detailed explanation

TODO
