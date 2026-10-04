---
id: emb-macros-0027
title: "How do you see what a macro actually expanded into?"
description: "Inspect the preprocessor output with gcc -E to see the actual macro expansion."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: gcc-cpp-invocation
    title: "GCC: Invocation (The C Preprocessor)"
    url: https://gcc.gnu.org/onlinedocs/cpp/Invocation.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Documents invoking GCC's preprocessor with -E and its output; other compilers may use different options."
---

## Short answer

Inspect the preprocessor output: `gcc -E file.c` (or `arm-none-eabi-gcc -E`). This option tells GCC to stop after preprocessing and emit the transformed translation unit.[^gcc-cpp-invocation]

This view helps trace included files and find the effects of macro substitution, such as missing parentheses or unexpected tokens. The output also contains headers and usually line markers, so it is more than a short list of macros.[^gcc-cpp-invocation] [^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
