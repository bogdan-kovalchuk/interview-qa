---
id: emb-dtypes-0098
title: "What happens with `uint32_t *ptr = (uint32_t*)0x40020000; *ptr = 0xFF;` without `volatile`?"
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

The compiler may optimize the write as an ordinary memory access because an external device is not part of C’s abstract machine.[^iso-c-n1570]

Without `volatile`, there is no guarantee that the intended write is preserved as a hardware access.

For a memory-mapped register, use a pointer to a `volatile` type, such as `volatile uint32_t *reg`; this requires the relevant accesses under C’s rules, but does not by itself guarantee the correct address, atomicity, or required ordering.[^iso-c-n1570]

## Detailed explanation

TODO
