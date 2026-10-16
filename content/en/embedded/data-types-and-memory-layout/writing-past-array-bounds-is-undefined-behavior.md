---
id: emb-dtypes-0016
title: "What is the danger here? `int arr[10]; arr[10] = 0;`"
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

<span class="warn">`arr[10]` has undefined behavior.</span> For `int arr[10]`, valid indices are `0..9`.[^iso-c-n1570]

The program may crash, corrupt data, or appear to work; it is not guaranteed to overwrite a neighboring local or return address because object placement varies by implementation.[^iso-c-n1570]

Use AddressSanitizer where supported and check the index before access.[^iso-c-n1570]

## Detailed explanation

TODO
