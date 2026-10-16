---
id: emb-volconst-0056
title: "What does `static const` mean for a table inside a C file?"
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

**At file scope, `static` gives the identifier internal linkage, and `const` prevents modification through that identifier.**

For an embedded lookup table this is a common form: other translation units cannot see the symbol, and the compiler may place the table in a read-only section. Placement in Flash depends on the linker script and platform.

Rule: declare file-private immutable tables as `static const` unless they must be part of the external ABI.[^iso-c-n1570]

## Detailed explanation

TODO
