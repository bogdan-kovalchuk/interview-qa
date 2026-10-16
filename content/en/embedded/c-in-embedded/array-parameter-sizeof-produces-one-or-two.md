---
id: emb-cppfound-0016
title: "Trap: what value does sizeof(arr)/sizeof(arr[0]) produce in this function?"
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

`n = 1` (on 32-bit) or `n = 2` (on 64-bit).

In a function parameter, `int arr[]` ≡ `int *arr` – decay to a pointer, so `sizeof(arr) = sizeof(int*) = 4` (or 8), `sizeof(arr[0]) = sizeof(int) = 4`, and `4/4 = 1`.

<span class="warn">Not 8, not 256, not the array size</span> – only 1 or 2.

Always pass the size explicitly: `void f(int *arr, size_t n)`; safeguard: `_Static_assert` at the caller.[^embeddedinterviewlab]

## Detailed explanation

TODO
