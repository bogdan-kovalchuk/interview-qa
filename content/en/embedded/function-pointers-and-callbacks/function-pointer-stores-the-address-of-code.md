---
id: emb-fnptr-0001
title: "What is a function pointer in C?"
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

**A function pointer** designates a function of a particular type for indirect calls. The function type specifies its return type and parameters; C does not require an ordinary numeric code address.[^iso-c-n1570]

Unlike an object pointer, a function pointer has a pointer-to-function type, not a pointer-to-object type. Code can select a function and call it through the pointer; its representation is implementation-defined.[^iso-c-n1570]

Rule: the function type must be compatible with the call; similar declarations alone do not prove this.[^iso-c-n1570]

## Detailed explanation

TODO
