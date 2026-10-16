---
id: emb-dtypes-0094
title: "What is a tentative definition in C, and where does it end up?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-codegen-options
    title: "GCC: Options for Code Generation Conventions"
    url: https://gcc.gnu.org/onlinedocs/gcc/Code-Gen-Options.html
  - source_id: cpp-basic-def
    title: "C++ draft: Declarations and definitions"
    url: https://eel.is/c++draft/basic.def
---

## Short answer

**Tentative definition** is a file-scope object declaration without an initializer or `extern`, such as `int x;`. If no ordinary definition of the same identifier appears in that translation unit, C treats it as a definition with zero initialization; the standard does not require placement in `.bss`.[^iso-c-n1570]

In GCC, placement in a common block depends on `-fcommon`; with `-fno-common`, same-name definitions from multiple files can fail at link time. C++ has no tentative-definition concept.[^gcc-codegen-options] [^cpp-basic-def]

## Detailed explanation

TODO
