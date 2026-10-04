---
id: emb-macros-0036
title: "What does this code print?"
description: "Prints 3 instead of 2 because the expansion 2 + 2 / 2 follows operator precedence."
track: embedded
section: inline-and-macros
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
#define HALF(x) x / 2
printf("%d", HALF(2 + 2));
```

## Short answer

It prints `3`, <span class="warn">not 2</span>, because the macro argument is substituted without automatic parentheses.[^iso-c-n1570]

Expansion: `2 + 2 / 2`. Due to precedence, first `2 / 2 = 1`, then `2 + 1 = 3`. The expected result was `(2 + 2) / 2 = 2`, but the missing parentheses change the order of operations.[^iso-c-n1570]

Protection: `#define HALF(x) (((x)) / 2)` -> expands to `(((2 + 2)) / 2) = 2`.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
