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
#define STR(x) #x
```

## Short answer

<span class="warn">`#` stringifies the argument text before it is expanded</span>, so the built-in macro `__LINE__` never gets a chance to turn into a number.

Fix: add an intermediate level – expand first, then stringify:

```c
#define STR(x) #x
#define XSTR(x) STR(x)
// XSTR(__LINE__) -> "42"
```

This is the classic two-level stringification idiom.[^embeddedinterviewlab]

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
