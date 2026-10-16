---
id: emb-fnptr-0036
title: "Trap: can a callback be an ordinary nested function in standard C?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-nested-functions
    title: "GCC documentation: Nested Functions"
    url: https://gcc.gnu.org/onlinedocs/gcc/Nested-Functions.html
---

## Short answer

<span class="warn">No. ISO C does not define nested functions; GCC provides them as a GNU C extension.</span> [^iso-c-n1570] [^gcc-nested-functions]

GCC implements taking a nested function's address with trampolines; the address also becomes unsafe after the containing function exits.[^gcc-nested-functions]

Protection: use a file-scope `static` function and `void *context`; this keeps the callback independent of a GNU extension.[^iso-c-n1570]

## Detailed explanation

TODO
