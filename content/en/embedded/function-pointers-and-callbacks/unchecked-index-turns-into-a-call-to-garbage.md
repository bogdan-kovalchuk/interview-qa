---
id: emb-fnptr-0020
title: "Trap: what is wrong with a dispatch table without an index check?"
description: "An index outside the dispatch table causes undefined behavior; the result depends on the implementation and platform."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 4
reconciled_with:
  uk: 3
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
    applicability: "Authoritative reference for C array subscripting, array bounds, and out-of-bounds behavior; the concrete consequence is platform-dependent."
---

## Question code

```c
typedef void (*handler_t)(void);
static handler_t table[4];

table[opcode]();
```

## Short answer

<span class="warn">If `opcode >= 4`, subscripting is outside the array and the program has undefined behavior; the call target is not necessarily random.</span>

On Cortex-M the result could be a HardFault, an incorrect branch, or another failure, but the C standard guarantees no particular outcome.

Defense: check the index first, then check that the selected handler is not a null pointer; see the C rules for subscripting and calls.[^iso-c-n1570]

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
