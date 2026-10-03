---
id: emb-macros-0014
title: "Trap: why does `STR(__LINE__)` give `\"__LINE__\"` instead of the line number?"
description: "The # operator stringifies argument text before expansion so an intermediate level is needed to expand built-in macros first."
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
#define STR(x) #x
```

## Short answer

<span class="warn">`#` stringifies the argument spelling without expanding it first</span>, so `STR(__LINE__)` produces the string `"__LINE__"`.

To get the line number as text, add an intermediate level: expand the macro first, then stringify:

```c
#define STR(x) #x
#define XSTR(x) STR(x)
// XSTR(__LINE__) expands to the current line number as a string
```

This is the standard two-level stringification pattern.[^iso-c-n1570]

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
