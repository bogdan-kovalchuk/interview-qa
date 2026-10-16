---
id: emb-dtypes-0089
title: "What is type punning, and when is it undefined behavior in C++?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Type punning** means interpreting an object’s bytes as another type. In C, reading a different `union` member has an implementation-defined result; accessing the same storage through an incompatible pointer can violate effective-type rules. In C++, reading an inactive `union` member is generally not a permitted conversion technique; for trivially copyable types use `memcpy` or C++20 `std::bit_cast`, and ensure the target representation is valid.[^iso-c-n1570]

## Detailed explanation

TODO
