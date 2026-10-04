---
id: emb-macros-0017
title: "How do you write debug-only code that disappears completely in a release build?"
description: "Conditional compilation removes debug code entirely before compilation leaving zero flash and RAM overhead."
track: embedded
section: inline-and-macros
level: junior
type: mechanism
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
  - source_id: gcc-cpp-overview
    title: "GCC CPP: Overview"
    url: https://gcc.gnu.org/onlinedocs/cpp/Overview.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Explains preprocessing as a stage before compilation; it does not guarantee a particular binary size for every toolchain."
---

## Question code

```c
#ifdef DEBUG
  #define DBG(fmt, ...) printf(fmt, ##__VA_ARGS__)
#else
  #define DBG(fmt, ...)
#endif
```

## Short answer

**Conditional compilation**: when `DEBUG` is defined, the macro expands to `printf`; otherwise the invocation becomes empty and is not passed to the compiler as C code.

This differs from `if (debug)`: the preprocessor removes text before compilation, but final firmware size also depends on other references and build settings.

Define `DEBUG` via a build flag (`-DDEBUG`) and check the release configuration separately.[^gcc-cpp-overview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
