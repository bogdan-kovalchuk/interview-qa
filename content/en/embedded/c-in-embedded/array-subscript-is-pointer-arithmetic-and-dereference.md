---
id: emb-cppfound-0031
title: "How are `arr[i]` and `*(arr+i)` related in standard C?"
track: embedded
section: c-in-embedded
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Per the C standard (§6.5.2.1): **`arr[i]` is defined as `*(arr+i)`**. This is not syntactic sugar – it is the exact definition of the subscript operator.

Consequences:
- `arr[2] == *(arr+2) == *(2+arr) == 2[arr]` – all equivalent;
- Indexing is simply pointer arithmetic + dereference;
- Negative indices (`arr[-1]`) are formally allowed if the pointer is already offset and the result points within the array.[^embeddedinterviewlab]

## Detailed explanation

TODO
