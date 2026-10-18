---
id: emb-cppfound-0039
title: "What does `memcpy(dst, src, sizeof(src))` do when `src` is an array parameter?"
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

<span class="warn">It copies only 4 or 8 bytes</span> (the pointer size), not the array size.

In a function parameter, `src` is `uint8_t*`, not an array. `sizeof(src) = sizeof(uint8_t*) = 4`. So `memcpy` copies only 4 bytes instead of N.

Correct approach: pass the size explicitly: `memcpy(dst, src, n * sizeof(src[0]))` or `memcpy(dst, src, n)` where `n` is a separate parameter.[^embeddedinterviewlab]

## Detailed explanation

TODO
