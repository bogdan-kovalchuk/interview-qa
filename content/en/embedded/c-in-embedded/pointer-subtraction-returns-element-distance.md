---
id: emb-cppfound-0049
title: "How does pointer arithmetic behave when subtracting two pointers?"
track: embedded
section: c-in-embedded
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Subtracting two pointers of the same type returns **ptrdiff_t** – the number of elements between them (not bytes).

`int *p = arr+4; int *q = arr+1; p - q = 3` (three `int` elements).

Condition: both pointers must point to the **same array** (or one-past-the-end). Subtracting pointers that point to different arrays/objects -> <span class="warn">undefined behavior</span>.

Application: `strlen`-like counting, offset between buffer elements.[^embeddedinterviewlab]

## Detailed explanation

TODO
