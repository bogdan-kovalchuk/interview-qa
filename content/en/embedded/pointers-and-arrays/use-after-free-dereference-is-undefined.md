---
id: emb-cppfound-0046
title: "Trap: what is wrong?"
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

## Question code

```c
free(ptr);
if(*ptr == 0)
```

## Short answer

<span class="warn">Use-after-free is undefined behavior.</span> After `free(ptr)`, the memory block is returned to the heap manager and may be immediately reused.

Reading `*ptr` is undefined behavior: it may return 0, the old value, or a new value from another malloc. In real code, it is a source of security vulnerabilities (type confusion, heap exploitation).

Rule: after `free`, always: `ptr = NULL;`; then `if(ptr != NULL && *ptr == 0)` is safe.[^embeddedinterviewlab]

## Detailed explanation

TODO
