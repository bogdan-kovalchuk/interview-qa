---
id: emb-cppfound-0050
title: "What does this print?"
description: "Why modifying and reading a pointer in one printf call is undefined behavior."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 4
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
    applicability: "Origin of the question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Question code

```c
int arr[5]={1,2,3,4,5};
int *p=arr;
printf("%d %d", *p++, *p);
```

## Short answer

<span class="warn">Undefined behavior</span> – the order of evaluation of `printf` arguments is not defined by the standard.

`p++` – post-increment: returns the current value and then increments. But there is no sequence point between evaluating `*p++` and `*p` within a single function call. The compiler may evaluate the arguments in any order.

The result depends on the compiler/platform. Better: `printf("%d %d", arr[0], arr[1]);`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
