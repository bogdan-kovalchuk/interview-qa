---
id: emb-macros-0030
title: "Why are `enum`/`const` often better than `#define` for named constants in C?"
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

**Enum enumerators and `const` objects are C declarations with a type and scope**, whereas `#define` substitutes preprocessing tokens and does not create a typed C identifier.[^iso-c-n1570]

`enum { MAX_CH = 8 };` provides an integer constant expression. A `const` object has a declared type, but in C it is not an integer constant expression for an ordinary array bound.[^iso-c-n1570]

Use `enum` for sets of integer constants, `const` for a typed object, and `#define` when you specifically need preprocessor behavior.[^iso-c-n1570]

## Detailed explanation

TODO
