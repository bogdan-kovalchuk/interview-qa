---
id: emb-patterns-0020
title: "What is the error struct pattern and when is it better than a plain code?"
description: "It stores not only the code but also context: the failing source line and the time"
track: embedded
section: common-code-patterns
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
typedef struct {
  err_t    code;
  uint16_t line;      // __LINE__
  uint32_t timestamp; // tick
} err_info_t;
```

## Short answer

**It stores not only the code but also context: the failing source line and the time.**

Useful for diagnostics: `record_error(code, __LINE__)` into a global `last_error` gives minimal overhead and the ability to understand exactly where the error occurred.

Rule: context-rich error info is for diagnosing complex or rare faults.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
