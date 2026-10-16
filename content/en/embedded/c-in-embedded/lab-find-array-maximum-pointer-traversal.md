---
id: emb-cppfound-0075
title: "Implement an array-maximum search using pointer traversal."
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

```c
int find_max(const int *arr, size_t n) {
    if(arr == NULL || n == 0) return INT_MIN;
    const int *p = arr;
    const int *end = arr + n;
    int max = *p++;
    while(p != end) {
        if(*p > max) max = *p;
        p++;
    }
    return max;
}
```

Key points: `const int*` – read-only, `size_t n` – explicit size, `arr + n` – one-past-the-end as sentinel. `INT_MIN` requires `<limits.h>`; in a real API it is better to return status separately from the value.[^embeddedinterviewlab]

## Detailed explanation

TODO
