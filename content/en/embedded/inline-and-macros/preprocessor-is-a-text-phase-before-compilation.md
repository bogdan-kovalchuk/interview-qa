---
id: emb-macros-0001
title: "What is the C preprocessor and when does it do its work?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-cpp-overview
    title: "GCC manual: The C Preprocessor, Overview"
    url: https://gcc.gnu.org/onlinedocs/cpp/Overview.html
  - source_id: gcc-cpp-invocation
    title: "GCC manual: The C Preprocessor, Invocation"
    url: https://gcc.gnu.org/onlinedocs/cpp/Invocation.html
---

## Short answer

**The preprocessor** is a text phase that runs before compilation and handles `#include`, `#define`, `#if` directives.

It processes preprocessing directives and expands macros, but does not check types or ordinary C/C++ semantics. An error may therefore become visible only after expansion, during later parsing or type checking.[^gcc-cpp-overview]

To inspect GCC's preprocessing output, use `gcc -E file.c`.[^gcc-cpp-invocation]

## Detailed explanation

TODO
