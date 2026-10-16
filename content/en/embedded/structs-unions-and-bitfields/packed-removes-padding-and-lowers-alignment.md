---
id: emb-structs-0011
title: "What is a `packed` struct?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: gcc-attributes
    title: "GCC: Common Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Packed structure** asks the compiler not to insert normal padding between fields or to reduce the struct alignment.

This is useful for wire-format headers, on-flash records, or a precisely specified binary layout. But packed can cause unaligned accesses: a `uint32_t` field may end up at offset 1, which on some MCUs is slow or even faults.

Rule: packed is applied at format boundaries, not as a universal way to save RAM. For internal data, it is better to reorder fields.[^gcc-attributes]

## Detailed explanation

TODO
