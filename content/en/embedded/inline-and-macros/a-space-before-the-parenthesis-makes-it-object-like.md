---
id: emb-macros-0040
title: "Trap: why is this not a function-like macro?"
description: "A space between the macro name and the opening parenthesis makes it object-like, so invocation text is pasted after the full replacement."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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
#define F (x) (x) * (x)
int r = F(3);
```

## Short answer

<span class="warn">The space between `F` and `(x)` makes it an object-like macro.</span>

The preprocessor sees the name `F` replaced with the entire text `(x) (x) * (x)`. Then `F(3)` expands to `(x) (x) * (x)(3)` – it uses an undefined `x`, an obvious error.

Fix: in a function-like macro the opening parenthesis `(` must follow the name immediately, with no space: `#define F(x) ((x) * (x))`.[^embeddedinterviewlab]

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
