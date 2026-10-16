---
id: emb-macros-0048
title: "How does the meaning of `inline` differ between C and C++?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cppreference-inline
    title: "cppreference: inline specifier"
    url: https://en.cppreference.com/w/cpp/language/inline
---

## Short answer

In C++, an `inline` function may be defined in multiple translation units (TUs) through a header when the definitions meet ODR (One Definition Rule) requirements; this is a standard way to define functions in a header.[^cppreference-inline][^embeddedinterviewlab]

In C (C99+) the rules are more complex: plain `inline` provides only an inline definition with no external symbol, so an `extern` declaration is needed in one TU, or more simply, `static inline`.

In C, `static inline` is often used for header functions; in C++, `inline` permits multiple definitions under ODR conditions.[^iso-c-n1570]

## Detailed explanation

TODO
