---
id: emb-dtypes-0100
title: "Trap: legal in C or C++? `union { float f; uint32_t u; } pun; pun.f = 1.0f; uint32_t r = pun.u;`"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cpp-union
    title: "C++ working draft: Unions"
    url: https://eel.is/c++draft/class.union.general
  - source_id: cpp-bit-cast
    title: "C++ working draft: bit_cast"
    url: https://eel.is/c++draft/bit.cast
---

## Short answer

In **C**, reading another union member reinterprets the corresponding bytes; the result is not a portable numeric conversion, and a trap representation cannot safely be read as a value.[^iso-c-n1570]

In **C++**, reading inactive member `u` after writing `f` has <span class="warn">undefined behavior</span> in this case; the common initial sequence exception does not apply.[^cpp-union]

Use `memcpy` to copy a representation in C; in C++20, `std::bit_cast` is available when the types have equal size and are trivially copyable.[^cpp-bit-cast]

## Detailed explanation

TODO
