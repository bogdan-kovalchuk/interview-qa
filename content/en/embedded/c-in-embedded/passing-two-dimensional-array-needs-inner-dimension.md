---
id: emb-cppfound-0029
title: "How should a 2D array be passed to a function to access element `[2][3]`?"
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

For a statically sized array you must specify the **inner dimension size**: `void f(int arr[][4], int rows) { arr[2][3] = 99; }` or equivalently: `void f(int (*arr)[4], int rows) { ... }`

Without the size the compiler does not know the row stride. `arr[i][j]` -> `*(*(arr+i)+j)` -> in memory: `arr + i*4*sizeof(int) + j*sizeof(int)`.

For a dynamic one: pass as `int *` and compute the offset manually.[^embeddedinterviewlab]

## Detailed explanation

TODO
