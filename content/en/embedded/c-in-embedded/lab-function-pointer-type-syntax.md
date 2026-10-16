---
id: emb-cppfound-0079
title: "How do you declare a pointer to a function taking `int` and returning `void`?"
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

## Short answer

`void (*fp)(int);` – this declaration means a pointer to a function. Reading: `fp` is a pointer (`*fp`) to a function (`(*fp)(int)`) that returns void. For convenience – `typedef`:

```c
typedef void (*callback_t)(int);
callback_t fp = my_func;
```

Without typedef for an array: `void (*table[8])(int);` – an array of 8 function pointers; call with `fp(42);` or `(*fp)(42);` – both are valid.[^embeddedinterviewlab]

## Detailed explanation

TODO
