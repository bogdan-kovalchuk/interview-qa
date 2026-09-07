---
id: emb-cppfound-0075
title: "Implement an array-maximum search using pointer traversal."
description: "A pointer-traversal implementation for finding the maximum array element."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
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

## Sources

<!-- generated from frontmatter -->
