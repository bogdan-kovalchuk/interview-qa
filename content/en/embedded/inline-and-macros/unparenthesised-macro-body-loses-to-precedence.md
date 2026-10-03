---
id: emb-macros-0004
title: "What does this code actually compute?"
description: "r equals 11 instead of 25 because the macro expands without parentheses and operator precedence changes the computation."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
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
#define SQUARE(x) x * x
int r = SQUARE(2 + 3);
```

## Short answer

`r == 11`, not <span class="warn">25</span>.

A macro is text substitution without parentheses, so `SQUARE(2 + 3)` expands to `2 + 3 * 2 + 3`. By precedence rules, `3 * 2 = 6` is computed first, then `2 + 6 + 3 = 11`.

Fix: `#define SQUARE(x) ((x) * (x))` – then the result is `((2 + 3) * (2 + 3)) = 25`.[^iso-c-n1570]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
