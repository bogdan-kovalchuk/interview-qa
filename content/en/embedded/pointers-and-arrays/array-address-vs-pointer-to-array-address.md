---
id: emb-cppfound-0043
title: "What value does `&arr` return, and how does it differ from `arr` when `int arr[8]`?"
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

Both expressions yield the **same numeric address** (the address of the first element of the array), but have different **types**:

`arr` -> decays to `int*`. `arr+1` -> +4 bytes (one int). `&arr` -> `int(*)[8]` (pointer to array). `&arr+1` -> +32 bytes (one array).

In practice: `&arr` is used to pass to a function that expects `int(*)[8]` – it preserves the array size in the type.[^embeddedinterviewlab]

## Detailed explanation

TODO
