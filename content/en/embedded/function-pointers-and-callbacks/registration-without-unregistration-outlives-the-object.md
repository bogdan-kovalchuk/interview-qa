---
id: emb-fnptr-0043
title: "Trap: what is wrong with registering a callback and never unregistering it?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cppreference-pointer
    title: "cppreference: Pointers"
    url: https://en.cppreference.com/w/cpp/language/pointer
  - source_id: cppcoreguidelines-lifetime
    title: "C++ Core Guidelines: Lifetime safety"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines
---

## Short answer

<span class="warn">The driver can invoke the callback after the module or object has been destroyed.</span>

Especially in C++ embedded: the object destructor may have finished, but the C HAL still holds `ctx = this`. The next interrupt calls the thunk with a dangling `this` pointer.

Defence: in the destructor or shutdown path, unregister the callback and disable interrupts or events before destroying state. Define ownership in the API.[^cppcoreguidelines-lifetime]

## Detailed explanation

TODO
