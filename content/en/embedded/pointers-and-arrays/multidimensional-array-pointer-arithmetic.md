---
id: emb-cppfound-0060
title: "What does this print?"
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
int arr[3][3]={{1,2,3},{4,5,6},{7,8,9}};
printf("%d", *(*(arr+1)+2));
```

## Short answer

`6`.

`arr+1` -> pointer to the second row `arr[1]` (type `int(*)[3]`). `*(arr+1)` -> decays to `int*`, points to `arr[1][0] = 4`. `*(arr+1)+2` -> points to `arr[1][2] = 6`. `*(*(arr+1)+2)` -> value = `6`.

Equivalent: `arr[1][2]`.[^embeddedinterviewlab]

## Detailed explanation

TODO
