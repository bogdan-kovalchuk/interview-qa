---
id: emb-cppfound-0030
title: "Trap: what is wrong?"
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
arr[5] = 0;
```

## Short answer

<span class="warn">Out-of-bounds write -> undefined behavior.</span> Valid indices: `0..4`, and `arr[5]` is beyond the array.

In memory `arr[5]` sits right after the array: it may be another local variable, a return address, a saved LR, so the consequences are silent data corruption or a crash on function return (a corrupted return address).

Protection: `-fsanitize=address`, explicit index checks, `static_assert(i < ARRAY_SIZE)`.[^embeddedinterviewlab]

## Detailed explanation

TODO
