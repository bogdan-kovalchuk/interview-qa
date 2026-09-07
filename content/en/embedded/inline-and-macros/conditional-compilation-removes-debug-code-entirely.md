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
updated: 2026-09-07
content_revision: 2
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
#ifdef DEBUG
  #define DBG(fmt, ...) printf(fmt, ##__VA_ARGS__)
#else
  #define DBG(fmt, ...)
#endif
```

## Short answer

**Conditional compilation**: with `DEBUG` the macro expands to `printf`, otherwise to nothing, and the code is removed entirely before compilation (zero flash/RAM).

This is better than `if (debug)` because it leaves no dead branches and no string literals in the firmware.

Rule: define `DEBUG` via a build flag (`-DDEBUG`), not in the code.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
