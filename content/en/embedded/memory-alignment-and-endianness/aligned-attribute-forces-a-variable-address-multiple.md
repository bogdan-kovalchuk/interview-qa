---
id: emb-align-0030
title: "What does `__attribute__((aligned(N)))` do for a variable?"
description: "For a supported target, asks GCC to give the variable alignment of at least N bytes."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 4
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: gcc-variable-attributes
    title: "GCC 12.5: Common Variable Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc-12.5.0/gcc/Common-Variable-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: "12.5"
    applicability: "Documents the GNU aligned attribute, power-of-two argument, and linker limitations; does not guarantee behavior for other compilers or targets."
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Question code

```c
uint8_t buf[64] __attribute__((aligned(32)));
```

## Short answer

**For a supported target, asks GCC to give the variable alignment of at least N bytes.**[^gcc-variable-attributes]

Used for DMA or cache-line buffers when an aligned address is required. This is a GNU compiler extension; standard C has `_Alignas`, but support for a particular value depends on the implementation and target.[^gcc-variable-attributes] [^iso-c-n1570]

`aligned` changes an alignment requirement, but does not select a memory region, configure DMA, or define a wire format. `packed` is a separate attribute with separate consequences.[^gcc-variable-attributes]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
