---
id: emb-cppfound-0055
title: "How can you implement `swap` for two `int` values using pointers?"
description: "How to swap two integers through pointer parameters."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 5
reconciled_with:
  uk: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and answer; answer not independently verified."
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
void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
```

Call: `int x=5, y=10; swap(&x, &y);` -> `x=10, y=5`.

Without tmp via XOR: `*a^=*b; *b^=*a; *a^=*b;` – but <span class="warn">if `a == b`, the value becomes zero</span> (both pointers alias one object and `x ^ x == 0`). Always pass addresses (via `&` at the caller), not values.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
