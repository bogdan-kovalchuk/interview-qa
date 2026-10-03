---
id: emb-macros-0012
title: "What does the stringification operator `#` do in a macro?"
description: "The # operator turns a macro argument into a string literal using the argument text as written before expansion."
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
#define STR(x) #x
printf("%s", STR(hello));
```

## Short answer

**`#x` turns the spelling of a macro argument into a string literal**: here `"hello"` is substituted.

It works only for a function-like macro parameter, without expanding macros inside the argument first. Whitespace is normalized, and quotes and backslashes are escaped.

For example, `STR(hello)` produces `"hello"`; expanding a nested macro first requires an extra level.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
