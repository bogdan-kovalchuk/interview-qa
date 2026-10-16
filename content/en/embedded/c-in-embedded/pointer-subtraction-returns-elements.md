---
id: emb-cppfound-0091
title: "Trap: what is printed?"
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
int arr[5];
int *p=arr+3;
int *q=arr+1;
printf("%td", p-q);
```

## Short answer

`2`. This is not a trap, but it tests understanding of pointer subtraction.

The real trap: people expect a <span class="warn">byte difference</span> (8 bytes) but get the **element count** (2). `p - q` = `(arr+3) - (arr+1) = 2`.

Byte difference: `2 * sizeof(int) = 8`. But `ptrdiff_t` returns elements; for a byte difference: `(char*)p - (char*)q` or `(uintptr_t)p - (uintptr_t)q`.[^embeddedinterviewlab]

## Detailed explanation

TODO
