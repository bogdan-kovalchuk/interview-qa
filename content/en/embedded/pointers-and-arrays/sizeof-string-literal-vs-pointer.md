---
id: emb-cppfound-0053
title: "What do `sizeof(\"hello\")` and `sizeof(char*)` return on 32-bit?"
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

`sizeof("hello")` -> **6**: a string literal is an array `{'h','e','l','l','o','\0'}`, and `sizeof` returns the array size including the null terminator.

`sizeof(char*)` -> **4**: the pointer size equals the platform word size.

Key point: `sizeof("hello")` does not decay to a pointer (sizeof is one of the three array decay exceptions), so we get the array size.[^embeddedinterviewlab]

## Detailed explanation

TODO
