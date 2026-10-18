---
id: emb-cppfound-0020
title: "What does this array-of-pointers example print?"
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
int a=1,b=2,c=3;
int *arr[3]={&a,&b,&c};
printf("%d",*arr[1]);
```

## Short answer

`2`.

`int *arr[3]` – an array of 3 pointers to `int`. `arr[1]` -> the second element = `&b`, so `*arr[1]` -> dereferencing `&b` -> the value of `b = 2`.

Storage: `arr` – an array of addresses (3 × 4 bytes = 12 bytes). Each element is a separate address; changing `*arr[1] = 99` -> modifies `b`.[^embeddedinterviewlab]

## Detailed explanation

TODO
