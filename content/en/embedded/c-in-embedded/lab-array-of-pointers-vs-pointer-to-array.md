---
id: emb-cppfound-0065
title: "What is the memory difference between `int *arr[5]` and `int (*arr)[5]`?"
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

`int *arr[5]` is an array of 5 pointers. Size: `5 × sizeof(int*) = 20 bytes`; each of the 5 elements is an address of some int and can point to different memory locations.

`int (*arr)[5]` is a single pointer to an array of 5 int. The size of `arr` = `sizeof(int*) = 4` bytes; `arr+1` -> offset by `5 × sizeof(int) = 20` bytes.

Reading rule: parentheses around `*arr` mean "pointer to".[^embeddedinterviewlab]

## Detailed explanation

TODO
