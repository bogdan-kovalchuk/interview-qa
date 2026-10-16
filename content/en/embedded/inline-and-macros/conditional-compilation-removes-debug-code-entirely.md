---
id: emb-macros-0017
title: "How do you write debug-only code that disappears completely in a release build?"
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
    title: "GCC CPP: Overview"
    url: https://gcc.gnu.org/onlinedocs/cpp/Overview.html
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
