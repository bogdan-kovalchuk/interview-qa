---
id: emb-volconst-0043
title: "What happens to this code in C?"
track: embedded
section: volatile-and-const
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
const int n = 8;
int a[n];
```

## Short answer

At block scope in C, this can be a VLA (variable length array) if the implementation supports VLAs; it is not necessarily a compile-time fixed array.[^iso-c-n1570]

`const int n` does not make `n` an integer constant expression in C the way many expect after C++. A VLA has a runtime-determined size; the standard does not require stack allocation, and embedded compilers may omit or prohibit VLAs.

Protection: for a compile-time size in C, use `#define N 8` or `enum { N = 8 }`.[^iso-c-n1570]

## Detailed explanation

TODO
