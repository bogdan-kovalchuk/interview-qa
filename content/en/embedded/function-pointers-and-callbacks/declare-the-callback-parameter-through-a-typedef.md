---
id: emb-fnptr-0014
title: "How do you declare a function that takes a callback `void cb(int)`?"
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

## Short answer

Yes. Direct parameter declaration, but a typedef is more readable:

```c
void register_cb(void (*cb)(int));

typedef void (*event_cb_t)(int);
void register_cb(event_cb_t cb);
```

Both declarations specify the same parameter type; a typedef only gives it a reusable name and makes the signature easier to read. It adds no checks or guarantees by itself.[^iso-c-n1570]

## Detailed explanation

TODO
