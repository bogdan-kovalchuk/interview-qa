---
id: emb-volconst-0061
title: "How does `const` help the compiler catch mistakes?"
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

**`const` lets the compiler diagnose a write through a const-qualified lvalue.** In C, this violates a language constraint, for which an implementation must issue a diagnostic; the standard does not require every such diagnostic to stop the build.[^iso-c-n1570]

For example, a parser with `const uint8_t *frame` cannot modify a byte through that pointer. This type restriction does not make memory physically read-only or configure the MPU.

Rule: `const` documents a read-only access contract and helps diagnose mistaken assignments; it is not hardware memory protection.[^iso-c-n1570]

## Detailed explanation

TODO
