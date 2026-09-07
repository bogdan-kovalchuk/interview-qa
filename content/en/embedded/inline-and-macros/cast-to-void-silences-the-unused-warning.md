---
id: emb-macros-0034
title: "What is the `UNUSED(x)` macro for and what does it look like?"
description: "Suppresses the unused parameter warning while explicitly showing the value is deliberately unused."
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
#define UNUSED(x) ((void)(x))
```

## Short answer

**Suppresses the 'unused parameter/variable' warning**, explicitly showing the intent that the value is deliberately unused.

Typical in callback signatures where some parameters are not needed: `void cb(void *ctx) { UNUSED(ctx); ... }`. A cast to `void` generates no code.

Rule: an explicit `UNUSED(x)` is better than globally disabling `-Wunused` – the warning remains useful elsewhere.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
