---
id: emb-macros-0015
title: "What is an include guard and which problem does it solve?"
description: "An include guard prevents a header from being included more than once in the same translation unit."
track: embedded
section: inline-and-macros
level: junior
type: concept
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
#ifndef SENSOR_H
#define SENSOR_H
/* вміст header */
#endif
```

## Short answer

**An include guard prevents a header from being included more than once** in the same translation unit.

Without it, a double `#include` causes <span class="warn">redefinition</span> of types, `struct`s and prototypes. On the first pass `SENSOR_H` is not yet defined -> the content is processed and the guard is defined; on subsequent passes the content is skipped.

Rule: every header needs a guard with a unique name, or `#pragma once`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
