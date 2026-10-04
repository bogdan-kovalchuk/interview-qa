---
id: emb-macros-0042
title: "What is a variadic macro and what is `__VA_ARGS__` for?"
description: "A variadic macro takes a variable argument count through ... and substitutes them into the body via VAARGS."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 4
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
  - source_id: gcc-variadic-macros
    title: "GCC: Variadic Macros"
    url: https://gcc.gnu.org/onlinedocs/gcc-8.1.0/cpp/Variadic-Macros.html
    accessed: 2026-10-04
    kind: official
    version: "GCC 8.1"
    applicability: "Explains __VA_ARGS__ substitution, the comma problem with an empty argument, and the GNU ##__VA_ARGS__ extension; this is not a portable replacement for C standard rules."
---

## Question code

```c
#define LOG(fmt, ...) \
  printf("[%lu] " fmt, tick(), __VA_ARGS__)
```

## Short answer

**A variadic macro accepts a variable number of arguments** via `...`, and `__VA_ARGS__` substitutes them into the body.

This allows building wrappers around `printf`-like functions, adding prefixes (timestamp, log level) and forwarding the remaining arguments.

In standard C, `__VA_OPT__` is available in C23; `##__VA_ARGS__` to remove the comma is a GNU extension, not a portable C rule.[^gcc-variadic-macros]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
