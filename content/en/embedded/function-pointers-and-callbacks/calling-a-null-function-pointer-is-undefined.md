---
id: emb-fnptr-0009
title: "Trap: what happens when a null function pointer is called?"
description: "Calling a null function pointer is undefined behavior."
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
void (*cb)(void) = NULL;
cb();
```

## Short answer

<span class="warn">Undefined behavior.</span>

On Cortex-M this is often an attempt to jump to address 0 or another invalid address, which may end in a HardFault. But the C standard guarantees no specific outcome: it is simply an incorrect call.

Defense: before an optional callback always check `if (cb != NULL) { cb(); }`, or register a default no-op callback.[^embeddedinterviewlab]

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
