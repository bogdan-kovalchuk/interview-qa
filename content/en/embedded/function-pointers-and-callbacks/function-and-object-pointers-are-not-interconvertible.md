---
id: emb-fnptr-0049
title: "Trap: why should you not store a function pointer in `void *`?"
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

<span class="warn">C does not guarantee portable conversion between a function pointer and the object pointer `void *`.</span>

Representations and sizes of pointer categories are implementation-dependent; ISO C defines conversion between `void *` and object pointers, but specifies no equivalent general rule for function pointers. POSIX has separate requirements for `dlsym`, but that is not a general ISO C rule or an embedded guarantee.[^iso-c-n1570]

Defence: keep function pointers in function pointer types and data pointers in `void *`. Do not put a callback address into a generic data pointer field.[^iso-c-n1570]

## Detailed explanation

TODO
