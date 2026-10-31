---
id: emb-cppfound-0071
title: "Is this code undefined behavior?"
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
int arr[3]={1,2,3};
int *p=arr;
p--;
printf("%d",*p);
```

## Short answer

<span class="warn">Yes, UB.</span> `p = arr` points to `arr[0]`. `p--` forms `arr - 1`, which is <span class="warn">outside the array</span>. Valid pointers for `arr[3]`: `arr` (= `arr + 0`) to `arr + 3` (one-past-the-end). `arr - 1` is UB already when formed, not only when dereferenced; the compiler may assume UB does not occur, leading to unpredictable optimizations, so `arr - 1` must never be formed.[^embeddedinterviewlab]

## Detailed explanation

TODO
