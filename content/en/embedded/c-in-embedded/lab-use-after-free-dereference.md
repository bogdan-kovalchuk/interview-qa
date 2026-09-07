---
id: emb-cppfound-0061
title: "What goes wrong when memory is read after free?"
description: "Why dereferencing freed heap memory is undefined behavior."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
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
    applicability: "Source question and answer; answer not independently verified."
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
int *p = malloc(sizeof(int)*10);
free(p);
printf("%d", p[0]);
```

## Short answer

<span class="warn">Use-after-free – undefined behavior.</span> After `free(p)` the memory is returned to the heap manager and may be immediately reused (for example, by the next `malloc`).

`p[0]` after `free`: may return 0 (the heap manager wrote metadata there), the old value, or crash. In a security context: a source of use-after-free exploits.

Protection: `free(p); p = NULL;`, then `if(p != NULL)` before access.[^embeddedinterviewlab]

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
