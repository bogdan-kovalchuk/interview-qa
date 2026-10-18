---
id: emb-cppfound-0016
title: "Trap: `void f(int arr[]) { int n = sizeof(arr)/sizeof(arr[0]); }` – яке значення `n`?"
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

## Short answer

`n = 1` (на 32-bit) або `n = 2` (на 64-bit).

У параметрі функції `int arr[]` ≡ `int *arr` – decay до вказівника, тож `sizeof(arr) = sizeof(int*) = 4` (або 8), `sizeof(arr[0]) = sizeof(int) = 4`, і `4/4 = 1`.

<span class="warn">Не 8, не 256, не розмір масиву</span> – лише 1 або 2.

Завжди передавай розмір явно: `void f(int *arr, size_t n)`; Захист: `_Static_assert` у caller.[^embeddedinterviewlab]

## Detailed explanation

TODO
