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

## Short answer

<span class="warn">The extra semicolon becomes part of the replacement text.</span>

`int a[SIZE];` expands to `int a[256;];` -> syntax error. And in `x = SIZE + 1;` you get `x = 256; + 1;`, which compiles but does the wrong thing.

Protection: never end an object-like macro with a semicolon: `#define SIZE 256`.[^embeddedinterviewlab]

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
