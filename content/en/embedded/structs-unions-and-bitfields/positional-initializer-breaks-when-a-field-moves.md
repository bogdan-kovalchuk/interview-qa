---
id: emb-structs-0031
title: "Trap: why is a positional initializer fragile?"
description: "Values are bound to field order, not to field names."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
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
struct Cfg { uint32_t baud; uint8_t parity; uint8_t stop; };
struct Cfg c = { 115200, 0, 1 };
```

## Short answer

<span class="warn">Values are bound to field order, not to field names.</span>

If someone inserts a new field between `baud` and `parity`, the initializer may remain syntactically valid, but the values will land in the wrong fields. In driver configs this creates silent runtime bugs.

Defence: for non-trivial structs use designated initializers: `{ .baud = 115200, .parity = 0, .stop = 1 }`.[^iso-c-n1570]

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
