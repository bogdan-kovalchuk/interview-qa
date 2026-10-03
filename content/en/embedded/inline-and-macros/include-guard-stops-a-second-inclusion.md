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
#ifndef SENSOR_H
#define SENSOR_H
/* вміст header */
#endif
```

## Short answer

**An include guard prevents a header from being included more than once** in the same translation unit.

Without it, repeated inclusion can repeat a type or object definition and cause a diagnostic; compatible repeated function declarations are allowed by themselves. On the first pass `SENSOR_H` is defined, and later passes skip the conditional block.

Use a guard name specific enough to the project to avoid macro collisions.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
