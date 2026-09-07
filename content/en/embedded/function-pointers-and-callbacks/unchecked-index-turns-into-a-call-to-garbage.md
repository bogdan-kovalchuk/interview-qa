---
id: emb-fnptr-0020
title: "Trap: what is wrong with a dispatch table without an index check?"
description: "Without an index check, an out-of-bounds read leads to an indirect call at a random address."
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
typedef void (*handler_t)(void);
static handler_t table[4];

table[opcode]();
```

## Short answer

<span class="warn">If `opcode >= 4`, there will be an out-of-bounds read and an indirect call to a random address.</span>

On Cortex-M this can cause a HardFault or, worse, jump to a valid but wrong code address. Dispatch tables are especially sensitive to input validation because data immediately becomes control flow.

Defense: check `if (opcode < ARRAY_SIZE(table) && table[opcode])`, otherwise call a default error handler.[^embeddedinterviewlab]

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
