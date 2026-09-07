---
id: emb-cppfound-0090
title: "Find the bug: will the outer pointer move?"
description: "Why changing a pointer parameter does not change the caller's pointer."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
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
void advance(char *p, int n){
  p += n;
}
```

## Short answer

<span class="warn">NO.</span> In C, parameters are passed **by value**. The function receives a copy of the pointer `p`. `p += n` modifies the local copy but not the original pointer in the caller.

To change the caller's pointer: a double pointer is needed: `void advance(char **p, int n){ *p += n; }` Call: `advance(&cursor, 5);`

A classic mistake when implementing parsers and stream handlers.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
