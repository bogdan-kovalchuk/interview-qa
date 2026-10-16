---
id: emb-macros-0027
title: "How do you see what a macro actually expanded into?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-cpp-invocation
    title: "GCC: Invocation (The C Preprocessor)"
    url: https://gcc.gnu.org/onlinedocs/cpp/Invocation.html
---

## Short answer

Inspect the preprocessor output: `gcc -E file.c` (or `arm-none-eabi-gcc -E`). This option tells GCC to stop after preprocessing and emit the transformed translation unit.[^gcc-cpp-invocation]

This view helps trace included files and find the effects of macro substitution, such as missing parentheses or unexpected tokens. The output also contains headers and usually line markers, so it is more than a short list of macros.[^gcc-cpp-invocation] [^iso-c-n1570]

## Detailed explanation

TODO
