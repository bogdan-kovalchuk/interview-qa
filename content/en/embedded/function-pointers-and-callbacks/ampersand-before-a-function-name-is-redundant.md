---
id: emb-fnptr-0008
title: "Do you need the `&` operator when assigning a function to a function pointer?"
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

**For an ordinary function-pointer assignment, the `&` operator is optional.**

`cb = foo;` and `cb = &foo;` have the same effect for a compatible function: the function designator converts to a pointer to function, while `&foo` explicitly takes the function's address.[^iso-c-n1570] Likewise, both `cb()` and `(*cb)()` are permitted call forms.

## Detailed explanation

TODO
