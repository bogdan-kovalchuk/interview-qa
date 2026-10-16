---
id: emb-cppfound-0081
title: "Trap: Is this valid in C99?"
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
int *p = &(int){5};
printf("%d", *p);
```

## Short answer

**Yes, valid** within the same block. `(int){5}` is a compound literal (C99): a temporary object with automatic block storage duration. <span class="warn">But dangling pointer</span> if the block scope is exited: `int *p; { p = &(int){5}; } *p; // UB – the block has ended`. GCC may not warn; safe usage: only within the same scope where the literal is defined.[^embeddedinterviewlab]

## Detailed explanation

TODO
