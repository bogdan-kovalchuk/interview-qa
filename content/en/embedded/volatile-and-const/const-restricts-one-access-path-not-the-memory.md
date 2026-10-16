---
id: emb-volconst-0049
title: "Why is `const` not a guarantee that an object never physically changes?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**`const` restricts writes through a specific typed access, but it does not prove that the physical memory will never change.**

An object can be mutable yet passed into a function as `const T *` so that the function does not modify it. And `volatile const` directly describes a case where firmware does not write, but hardware can change the value.

Rule: `const` is a restriction on typed access in C; actual memory permissions depend on the device and its configuration.[^iso-c-n1570]

## Detailed explanation

TODO
