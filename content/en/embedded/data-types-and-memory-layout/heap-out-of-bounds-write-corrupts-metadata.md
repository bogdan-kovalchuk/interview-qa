---
id: emb-dtypes-0075
title: "What happens? `int *p = (int*)malloc(10*sizeof(int)); p[10] = 0;`"
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

<span class="warn">A write outside the array has undefined behavior.</span> `p[10]` is not an element of an array of ten `int` values.[^iso-c-n1570]

`malloc(10 * sizeof(int))` requests space for ten elements, indexed 0 through 9. The C standard does not define what physically follows that object: the write may corrupt other data or fault, but heap metadata corruption is not guaranteed.[^iso-c-n1570]

During development, use available tools such as AddressSanitizer or guard regions to detect the error; their availability depends on the platform and runtime.[^iso-c-n1570]

## Detailed explanation

TODO
