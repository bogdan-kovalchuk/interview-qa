---
id: emb-dtypes-0006
title: "Why is `const char*` preferred over `char*` for a string literal?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cpp-draft-string-literals
    title: "C++ working draft, [lex.string]"
    url: https://eel.is/c++draft/lex.string
  - source_id: gcc-write-strings
    title: "GCC 16.1 Warning Options: -Wwrite-strings"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Warning-Options.html
---

## Short answer

In C, the string literal `"hello"` has type `char[6]`, but the standard prohibits modifying its array: an attempt has <span class="warn">undefined behavior</span>; the standard does not specify where an implementation stores the literal. In C++, a string literal has type `const char[6]`, so `const char *p = "hello";` preserves that restriction in the type system. In C, `char *p = "hello";` is allowed for compatibility, but writing through that pointer still has undefined behavior.[^iso-c-n1570] [^cpp-draft-string-literals]

## Detailed explanation

TODO
