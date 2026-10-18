---
id: emb-cppfound-0083
title: "What are the addresses of arr, &arr, arr+1, and &arr+1 for int arr[4]?"
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

`arr` -> `0x1000` (decays to `int*`, points to arr[0]). `&arr` -> `0x1000` (points to the entire array, type `int(*)[4]`). Same address, different type!

`arr+1` -> `0x1004` (step = `sizeof(int) = 4`), `&arr+1` -> `0x1010` (step = `sizeof(int[4]) = 16`).

This is where the type difference shows: same starting address, different step.[^embeddedinterviewlab]

## Detailed explanation

TODO
