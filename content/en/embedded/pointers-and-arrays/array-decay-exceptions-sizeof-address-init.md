---
id: emb-cppfound-0012
title: "In which three contexts does an array not decay to a pointer?"
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

An array stays an array and **does not decay** in three cases:

1. `sizeof(arr)` – returns the total size of the array in bytes, not the pointer size;
2. `&arr` – returns a pointer to the array `int(*)[N]`, not `int*`;
3. String literal initialization: `char arr[] = "hi"` – copies the characters into the array.

Remember these three exceptions – they come up often in interviews.[^embeddedinterviewlab]

## Detailed explanation

TODO
