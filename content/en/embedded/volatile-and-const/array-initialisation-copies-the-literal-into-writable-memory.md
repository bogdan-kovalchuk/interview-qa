---
id: emb-volconst-0031
title: "How do `const char *p = \"OK\"` and `char p[] = \"OK\"` differ?"
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

**`const char *p` points to a read-only string literal, while `char p[]` creates a mutable array with a copy of the characters.**

In the first case, `p[0] = 'N'` is forbidden by the type. In the second case, the array holds `'O'`, `'K'`, `'\0'` in its own storage, and `p[0] = 'N'` is allowed.

Embedded implication: the literal may reside in Flash, while a mutable array typically requires RAM.[^iso-c-n1570]

## Detailed explanation

TODO
