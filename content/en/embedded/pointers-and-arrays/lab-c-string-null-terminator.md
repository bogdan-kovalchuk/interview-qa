---
id: emb-cppfound-0072
title: "How is a C string stored in memory, and what is the role of the null terminator?"
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

A string in C is an array of characters where the last element is **'\0' (null-terminator)**, a byte with value 0. "hello" -> `['h','e','l','l','o','\0']` – 6 bytes in memory. The null-terminator signals to standard functions (`strlen`, `strcpy`, `printf %s`) where the string ends; without '\0' – reading goes out of bounds -> UB. String literals automatically have '\0'; when filling manually: `buf[n] = '\0';` is mandatory.[^embeddedinterviewlab]

## Detailed explanation

TODO
