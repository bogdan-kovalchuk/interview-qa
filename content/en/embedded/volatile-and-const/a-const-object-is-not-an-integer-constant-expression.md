---
id: emb-volconst-0042
title: "Trap: why does `const` in C not mean compile-time constant everywhere?"
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

<span class="warn">In C, `const` restricts modification through that identifier, but the object’s value does not become an integer constant expression.</span>[^iso-c-n1570]

For example, `const int n = 10;` is not an integer constant expression in C and cannot serve as the size of an ordinary file-scope array where one is required. C++ rules differ. In C, an integer constant, `enum`, or `#define` is commonly used for a fixed size.

Protection: do not confuse restricted writes through `const` with the language requirement for an integer constant expression.[^iso-c-n1570]

## Detailed explanation

TODO
