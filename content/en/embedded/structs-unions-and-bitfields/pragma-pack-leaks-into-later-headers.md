---
id: emb-structs-0047
title: "Trap: what is wrong with `#pragma pack` in a public header used carelessly?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-structure-layout-pragmas
    title: "GCC documentation: Structure-Layout Pragmas"
    url: https://gcc.gnu.org/onlinedocs/gcc/Structure-Layout-Pragmas.html
---

## Short answer

<span class="warn">It can change packing for subsequent structs in other code.</span>

In GCC, `#pragma pack(n)` affects the alignment of subsequent `struct` and `union` declarations; if the prior state is not restored, it can change types declared later in the same translation unit.[^gcc-structure-layout-pragmas]

Surround the required type with `#pragma pack(push, 1)` and `#pragma pack(pop)`, check support in the target compiler, and assert expected `sizeof` and field offsets.[^gcc-structure-layout-pragmas]

## Detailed explanation

TODO
