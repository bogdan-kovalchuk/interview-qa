---
id: emb-cppfound-0084
title: "Why should malloc always be checked for NULL?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
---

## Short answer

`malloc` returns **NULL** on allocation failure (no memory, heap fragmentation). If not checked and NULL is dereferenced -> <span class="warn">HardFault on MCU</span>.

```c
int *p = malloc(n * sizeof(int));
if(p == NULL) { error_handler(); return; }
```

In embedded: malloc can fail even for small requests due to fragmentation; safety-critical standards forbid malloc altogether – but if you use it, the check is mandatory.[^embeddedinterviewlab]

## Detailed explanation

TODO
