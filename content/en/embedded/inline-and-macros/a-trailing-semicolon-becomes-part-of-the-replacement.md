---
id: emb-macros-0029
title: "Trap: what is wrong with `#define SIZE 256;`?"
description: "A trailing semicolon becomes part of the replacement text and causes syntax errors or silent bugs."
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

## Short answer

<span class="warn">The extra semicolon becomes part of the replacement text.</span>

`int a[SIZE];` expands to `int a[256;];`, which is syntactically invalid. In `x = SIZE + 1;`, it becomes `x = 256; + 1;`: the assignment sets `x` to 256, while `+ 1;` is a separate expression with no useful effect.[^iso-c-n1570]

Protection: do not put a semicolon in an object-like macro's replacement list: `#define SIZE 256`.[^iso-c-n1570]

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
