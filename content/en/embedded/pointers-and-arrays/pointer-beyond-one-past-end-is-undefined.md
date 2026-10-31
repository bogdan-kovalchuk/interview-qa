---
id: emb-cppfound-0041
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
int arr[4]={0};
int *p=arr;
p+=5;
*p=1;
```

## Short answer

<span class="warn">Yes, undefined behavior</span> (even without dereferencing).

Forming the pointer `p += 5` goes beyond the array by more than one: `arr` has 4 elements, so valid pointers are `arr` through `arr+4` (inclusive of "one-past-the-end"). The expression `arr+5` is undefined behavior already at address formation.

One-past-the-end (`arr+4`) – may be formed, but <span class="warn">must not be dereferenced</span>.[^embeddedinterviewlab]

## Detailed explanation

TODO
