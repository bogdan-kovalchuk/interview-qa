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

**An error structure can store a code together with diagnostic context.**

For example, `record_error(code, __LINE__)` can record where a fault was detected; a global `last_error` stores only the latest record and needs coordination when accessed concurrently.

Such context helps diagnosis when its fields, size, and access rules fit the target platform.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
