---
id: emb-cppfound-0013
title: "What does this example print?"
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
int arr[3] = {1,2,3};
printf("%d %d", arr[2], *(arr+2));
```

## Short answer

Both expressions print **3** and are fully equivalent per the C standard.

`arr[2]` -> the standard defines it as `*(arr+2)`: `2 * sizeof(int) = 8` bytes are added to the address `arr`, then dereferenced.

Therefore even `2[arr]` -> `*(2+arr)` -> 3 – also valid (due to commutativity of addition, although unreadable).[^embeddedinterviewlab]

## Detailed explanation

TODO
