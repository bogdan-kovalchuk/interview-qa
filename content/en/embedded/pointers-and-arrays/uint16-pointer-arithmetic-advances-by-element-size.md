---
id: emb-cppfound-0022
title: "What address will `p` have after: `uint16_t arr[4]; uint16_t *p = arr; p += 2;`?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

If `arr` is at address `0x2000` -> `p = 0x2000 + 2 * sizeof(uint16_t) = 0x2000 + 4 = 0x2004`.

The pointer arithmetic step for `uint16_t*` is 2 bytes. `p += 2` -> offset of 2 elements × 2 bytes = 4 bytes.

Now `p` points to `arr[2]`. Note: steps are always in "type elements", not bytes.[^embeddedinterviewlab]

## Detailed explanation

TODO
