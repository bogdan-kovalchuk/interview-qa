---
id: emb-fnptr-0016
title: "Trap: what is wrong with calling a callback through an incompatible signature?"
description: "Calling through a function pointer of an incompatible type is undefined behavior."
track: embedded
section: function-pointers-and-callbacks
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
void f(int x);
void (*cb)(void) = (void (*)(void))f;
cb();
```

## Short answer

<span class="warn">Calling through a function pointer of an incompatible type is undefined behavior.</span>

Even if the function address is physically correct, the calling convention expects different arguments, return value, or register usage. On an embedded ABI this can corrupt the stack/registers or pass garbage values.

Defense: do not fix the `-Wincompatible-pointer-types` warning with a cast. Write an adapter function with the correct signature.[^embeddedinterviewlab]

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
