---
id: emb-fnptr-0004
title: "What does this typedef mean?"
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
typedef void (*timer_cb_t)(void *ctx);
```

## Short answer

**`timer_cb_t`** is a pointer-to-function type that takes `void *ctx` and returns `void`.

After this you can write `timer_cb_t cb;`, `void timer_start(timer_cb_t cb, void *ctx);`. Such a typedef dramatically reduces noise in driver APIs and makes the callback contract visible.

Declare the callback type once in a header; its declaration must describe a compatible function signature.[^iso-c-n1570]

## Detailed explanation

TODO
