---
id: emb-cppfound-0051
title: "Trap: UB?"
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
int arr[4]={1,2,3,4};
int *p=arr;
int *q=arr+5;
```

## Short answer

<span class="warn">Yes, undefined behavior already when forming `arr+5`</span>.

For array `arr[4]` (4 elements), valid pointers are: `arr` through `arr+4` inclusive (one-past-the-end). `arr+5` goes beyond one-past-the-end -> <span class="warn">undefined behavior even without dereferencing</span>.

The compiler may use this assumption for optimization, leading to unpredictable behavior. GCC with `-fsanitize=undefined` will detect it.[^embeddedinterviewlab]

## Detailed explanation

TODO
