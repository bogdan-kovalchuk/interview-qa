---
id: emb-fnptr-0047
title: "How do you declare an array of four pointers to `void handler(void)` functions?"
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

Yes. Direct array declaration, or more readably through a typedef:

```c
void (*handlers[4])(void);

typedef void (*handler_t)(void);
handler_t handlers[4];
```

Rule: in complex declarations of a function pointer array, using a typedef is often clearer.[^iso-c-n1570]

## Detailed explanation

TODO
