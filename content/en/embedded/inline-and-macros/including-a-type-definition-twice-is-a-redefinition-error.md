---
id: emb-macros-0039
title: "Trap: what happens if a header defining a `struct` is included twice without an include guard?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">Redefining a `struct` tag with a body</span> in the same translation unit violates a C constraint; C11 permits redeclaring a typedef name for a compatible type.

Double inclusion happens easily through transitive paths: `a.h` and `b.h` both include `types.h`, and `main.c` includes both. Without a guard the contents of `types.h` are processed twice.

Protection: wrap every header in an `#ifndef` guard so later `#include` directives skip its body.[^iso-c-n1570]

## Detailed explanation

TODO
