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
updated: 2026-09-07
content_revision: 3
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Question code

```c
#define LOG(fmt, ...) \
  printf("[%lu] " fmt, tick(), __VA_ARGS__)
```

## Short answer

**A variadic macro accepts a variable number of arguments** via `...`, and `__VA_ARGS__` substitutes them into the body.

This allows building wrappers around `printf`-like functions, adding prefixes (timestamp, log level) and forwarding the remaining arguments.

Rule: to handle "zero arguments" correctly, use `##__VA_ARGS__` (GNU) or `__VA_OPT__` (C23/C++20).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
