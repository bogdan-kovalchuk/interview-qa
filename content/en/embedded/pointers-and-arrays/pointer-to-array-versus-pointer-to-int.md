---
id: emb-cppfound-0015
title: "What is int (*p)[8] and how does it differ from int *p?"
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

`int *p` is a pointer to `int`, so `p+1` -> +4 bytes (one `int`), while `int (*p)[8]` is a **pointer to an array** of 8 `int`, where `p+1` -> +32 bytes (one array of 8 elements).

Usage: when working with 2D arrays: `int arr[3][8]; int (*p)[8] = arr;`. `p[1]` -> second row; `p[1][3]` -> `arr[1][3]`.

Reading rule: `(*p)` -> "pointer to" (parentheses matter because of operator precedence).[^embeddedinterviewlab]

## Detailed explanation

TODO
