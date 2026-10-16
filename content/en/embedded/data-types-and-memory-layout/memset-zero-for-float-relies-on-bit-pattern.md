---
id: emb-dtypes-0061
title: "What's wrong with `memset(ptr, 0, sizeof(*ptr))` to zero a `float` field in a struct?"
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

Formally: `memset` sets all bytes to 0. IEEE 754 `0.0f` = bit pattern `0x00000000` -> works in practice.

However: the C standard does not guarantee that float zero = all zero bytes (theoretically). A bigger problem: `memset(struct_ptr, 0, sizeof(*struct_ptr))` for a struct with `void*` - <span class="warn">NULL pointer</span> is not guaranteed to have bit-pattern 0x0 by the standard (although practically it does).

Better practice: explicit initialization of each field.[^iso-c-n1570]

## Detailed explanation

TODO
