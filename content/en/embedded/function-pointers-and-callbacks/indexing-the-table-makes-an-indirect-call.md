---
id: emb-fnptr-0019
title: "What does this dispatch table print?"
description: "The dispatch table prints 42 because ops[1] points to dbl."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: mechanism
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
int inc(int x) { return x + 1; }
int dbl(int x) { return x * 2; }
int (*ops[])(int) = { inc, dbl };
printf("%d", ops[1](21));
```

## Short answer

Prints `42`.

`ops[1]` is a pointer to `dbl`. The call `ops[1](21)` performs an indirect call and returns `21 * 2`.

Rule: an array of function pointers must contain functions with the same compatible signature. For different signatures, wrappers or variant dispatch are needed.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
