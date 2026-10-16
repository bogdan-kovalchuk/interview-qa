---
id: emb-fnptr-0046
title: "Can you have an array of functions in C?"
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

<span class="warn">No, an array of functions is impossible; you can have an array of function pointers.</span>

`void handlers[4](void);` is invalid: the array element type would be a function type, but array elements must be objects. A pointer to a function is an object type, so `void (*handlers[4])(void);` declares an array of four such pointers.[^iso-c-n1570]

Store the pointers, rather than trying to store functions as array values.[^iso-c-n1570]

## Detailed explanation

TODO
