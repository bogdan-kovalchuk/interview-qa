---
id: emb-cppfound-0024
title: "What does this print?"
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

## Question code

```c
int arr[3][4];
printf("%zu", sizeof(arr));
```

## Short answer

**48** bytes.

`arr` is a 2D array: 3 rows × 4 columns × `sizeof(int) = 4` bytes = 48B.

`sizeof(arr[0])` = `sizeof(int[4])` = 16B (one row), `sizeof(arr[0][0])` = `sizeof(int)` = 4B.

Row count: `sizeof(arr)/sizeof(arr[0]) = 48/16 = 3`. This trick works only in the same scope where the array is declared.[^embeddedinterviewlab]

## Detailed explanation

TODO
