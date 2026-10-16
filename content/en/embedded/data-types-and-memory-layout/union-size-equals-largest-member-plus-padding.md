---
id: emb-dtypes-0052
title: "How much memory does a union take, and how is its size computed?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-attributes-packed
    title: "GCC: Common Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
---

## Short answer

The C standard requires `sizeof(union)` to be sufficient for its largest member, but the exact value and alignment are implementation-defined; do not use a universal “largest plus padding” formula.[^iso-c-n1570]

All union members occupy the same memory region.

For example, `union { char c; int x; double d; }` has size at least `sizeof(double)`, but the claim “exactly 8” depends on the ABI.

At a time, a union stores a value of no more than one member; rules for reading a different member depend on the language and case.[^iso-c-n1570]

## Detailed explanation

TODO
