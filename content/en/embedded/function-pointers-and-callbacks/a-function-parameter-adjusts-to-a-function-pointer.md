---
id: emb-fnptr-0015
title: "What does the function parameter `void cb(int)` mean in a declaration?"
track: embedded
section: function-pointers-and-callbacks
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
void register_cb(void cb(int));
```

## Short answer

In function parameters it adjusts to a function pointer: nearly equivalent to `void register_cb(void (*cb)(int));`.

Functions are not passed by value. A function-type parameter in a function prototype is automatically converted to a pointer to function. This is similar to an array parameter, which decays to a pointer.

Rule: for clarity in callback APIs, prefer pointer syntax or a typedef.[^embeddedinterviewlab] [^iso-c-n1570]

## Detailed explanation

TODO
