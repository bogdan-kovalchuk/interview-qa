---
id: emb-fnptr-0039
title: "How does a C++ pointer to member function differ from an ordinary function pointer?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cpp-member-pointer
    title: "C++ working draft: Pointers to members and pointer-to-member operators"
    url: https://eel.is/c++draft/dcl.mptr
---

## Short answer

**A pointer to member function needs an object instance to be called.**

`void (Class::*pmf)()` has a distinct type from `void (*)()`: the first is a pointer to member, while the second is a pointer to function. A pointer to member is applied to an object with `.*` or `->*`, then the result is called.[^cpp-member-pointer]

For a C callback from a C++ class, use a static member-function wrapper and pass `this` through a context pointer; a static member function can have an ordinary function pointer type.[^cpp-member-pointer]

## Detailed explanation

TODO
