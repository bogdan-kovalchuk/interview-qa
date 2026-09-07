---
id: emb-macros-0046
title: "Trap: how many times is `a` incremented?"
description: "There is no reliable answer because the macro expands its argument twice, producing unsequenced modifications and undefined behavior."
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
#define SQR(x) ((x) * (x))
int a = 2;
int b = SQR(a++);
```

## Short answer

<span class="warn">There is no reliable answer: this is undefined behavior.</span>

The macro substitutes the argument in two places: `((a++) * (a++))`. Parentheses save you from precedence issues, but not from double evaluation. Two increments of the same scalar object within one expression are unsequenced relative to each other, so the C standard defines neither the multiplication result nor the final value of `a`.

Fix: correct parentheses do not cure side effects; for arguments with effects, use a `static inline` function or a local variable assigned before the macro.[^embeddedinterviewlab]

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
