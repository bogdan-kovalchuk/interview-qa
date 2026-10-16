---
id: emb-dtypes-0070
title: "What does `sizeof(struct { char a; char b; int c; })` return on a typical 32-bit ABI with 4-byte int alignment?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: gnu-c-struct-layout
    title: "GNU C Introduction and Reference Manual: Structure Layout"
    url: https://www.gnu.org/software/c-intro-and-ref/manual/html_node/Structure-Layout.html
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Under the stated ABI, the result is **8 bytes**: `a` and `b` have offsets 0 and 1, two padding bytes align `c` at offset 4, and there is no trailing padding.[^gnu-c-struct-layout] Reordering to `char`, `int`, `char` gives 12 bytes on the same typical ABI because padding appears before and after `int`.[^gnu-c-struct-layout]

C does not guarantee this layout on every system: size and alignment depend on ABI, packing options, and attributes. Ordering fields by decreasing alignment often reduces padding, but verify offsets and `sizeof` with the target compiler.[^iso-c-n1570][^gnu-c-struct-layout]

## Detailed explanation

TODO
