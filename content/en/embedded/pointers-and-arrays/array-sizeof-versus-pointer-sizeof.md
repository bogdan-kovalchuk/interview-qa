---
id: emb-cppfound-0010
title: "What do sizeof(arr) and sizeof(p) return for int arr[8] and int *p = arr?"
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

`sizeof(arr)` -> **32** (8 elements × 4 bytes = 32B). `sizeof` on a real array returns the total size in bytes.

`sizeof(p)` -> **4** (or 8 on 64-bit). A pointer stores only an address – its size equals the architecture's word size.

Key difference: array and pointer have the same element type, but `sizeof` gives completely different results.[^embeddedinterviewlab]

## Detailed explanation

TODO
