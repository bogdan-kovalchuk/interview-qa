---
id: emb-cppfound-0055
title: "How can you implement `swap` for two `int` values using pointers?"
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
