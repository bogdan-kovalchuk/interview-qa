---
id: emb-macros-0005
title: "Trap: what is wrong with the call `MAX(++x, y)`?"
description: "Double evaluation in a function-like macro causes arguments with side effects to execute more than once."
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
#define MAX(a, b) ((a) > (b) ? (a) : (b))
```

## Short answer

<span class="warn">Double evaluation</span>: the parameter `a` appears twice in the body, so `++x` executes twice when the condition is true.

Expansion: `((++x) > (y) ? (++x) : (y))` – `x` is incremented a second time in the true branch. Any argument with a side effect (`++`, `--`, a function call, reading a volatile register) produces an unexpected result.

Fix: use a `static inline` function – it evaluates its argument exactly once.[^embeddedinterviewlab]

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
