---
id: emb-cppfound-0061
title: "What goes wrong when memory is read after free?"
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
int *p = malloc(sizeof(int)*10);
free(p);
printf("%d", p[0]);
```

## Short answer

<span class="warn">Use-after-free – undefined behavior.</span> After `free(p)` the memory is returned to the heap manager and may be immediately reused (for example, by the next `malloc`).

`p[0]` after `free`: may return 0 (the heap manager wrote metadata there), the old value, or crash. In a security context: a source of use-after-free exploits.

Protection: `free(p); p = NULL;`, then `if(p != NULL)` before access.[^embeddedinterviewlab]

## Detailed explanation

TODO
