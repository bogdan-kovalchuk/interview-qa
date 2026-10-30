---
id: emb-cppfound-0093
title: "What does this array subscript expression print?"
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
int arr[4]={10,20,30,40};
printf("%d %d",*(arr+3), arr[3]);
```

## Short answer

Both print `40`.

`*(arr+3)` -> pointer arithmetic: offset by 3 elements, dereference = `arr[3] = 40`. `arr[3]` -> subscript operator, by definition = `*(arr+3)`.

They are **identical per the standard**. The compiler generates the same machine code for both variants.[^embeddedinterviewlab]

## Detailed explanation

TODO
