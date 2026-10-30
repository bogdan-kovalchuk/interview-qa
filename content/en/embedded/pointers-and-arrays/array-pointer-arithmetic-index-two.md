---
id: emb-cppfound-0008
title: "What does this pointer arithmetic example print?"
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

## Question code

```c
int arr[5] = {10,20,30,40,50};
int *p = arr;
printf("%d", *(p+2));
```

## Short answer

`30`.

`arr` decays to a pointer to the first element. `p = arr` -> `p` points to `arr[0]`.

`p+2` -> pointer to `arr[2]` (step of `2 * sizeof(int) = 8` bytes on 32-bit). `*(p+2)` -> dereference -> `arr[2] = 30`.

Per the standard: `arr[i] ≡ *(arr+i) ≡ *(i+arr) ≡ i[arr]` – all four forms are equivalent.[^embeddedinterviewlab]

## Detailed explanation

TODO
