---
id: emb-cppfound-0054
title: "What is pointer aliasing, and how does it affect optimization?"
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

**Pointer aliasing** – a situation where two or more pointers refer to the same memory location.

Strict aliasing rule (C99 §6.5): the compiler may assume that pointers of different types do not alias (except for `char*`/`unsigned char*`). This allows more aggressive optimization.

Violation: `int x; float *fp = (float*)&x; *fp = 1.0f;` -> undefined behavior.

Protection: `memcpy` for type punning, `char*` for byte access, `restrict` for an explicit no-aliasing guarantee.[^embeddedinterviewlab]

## Detailed explanation

TODO
