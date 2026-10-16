---
id: emb-macros-0045
title: "Why are compiler errors inside a macro hard to read?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-preprocessor-options
    title: "GCC: Preprocessor Options"
    url: https://gcc.sourceware.org/onlinedocs/gcc/Preprocessor-Options.html
---

## Short answer

**The error points to the expanded code, not to the `#define` line.**

The compiler analyzes tokens after preprocessor substitution, and modern compilers often show the expansion chain with both the call site and definition. Nested macros add more levels to that chain, making the error harder to read.

With GCC, `gcc -E` prints the preprocessed output, and `-ftrack-macro-expansion` controls tracking token locations in diagnostics. For nontrivial logic, choose a typed `static inline` function, which is easier to debug as ordinary code.[^gcc-preprocessor-options]

## Detailed explanation

TODO
