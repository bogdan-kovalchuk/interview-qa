---
id: emb-fnptr-0009
title: "Trap: what happens when a null function pointer is called?"
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
void (*cb)(void) = NULL;
cb();
```

## Short answer

<span class="warn">Undefined behavior.</span>

The C standard specifies no outcome for this call: it is undefined behavior, and the concrete response depends on the implementation and platform.[^iso-c-n1570]

Defense: check `cb != NULL` before an optional call, or give the API a guaranteed no-op callback.

## Detailed explanation

TODO
