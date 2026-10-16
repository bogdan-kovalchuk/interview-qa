---
id: emb-fnptr-0035
title: "Can a callback be a `static` function?"
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

**Yes.**

`static` at file scope gives the function internal linkage, but its address can still be passed as a callback within the same translation unit. Another translation unit cannot refer to its name, but a callback that has received the address can call it.[^iso-c-n1570]

For example, a file-scope `static` handler can be passed to a local driver or scheduler without exporting its name to other translation units. `static` does not change the function or pointer type; it restricts the linkage of the name.[^iso-c-n1570]

## Detailed explanation

TODO
