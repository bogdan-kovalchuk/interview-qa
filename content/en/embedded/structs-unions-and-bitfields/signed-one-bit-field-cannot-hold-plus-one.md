---
id: emb-structs-0022
title: "Trap: why is a one-bit signed bit-field almost always a trap?"
description: "A 1-bit signed field cannot represent +1 in the two's complement model."
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
struct F {
    signed int flag : 1;
};
```

## Short answer

<span class="warn">In two's complement, a 1-bit signed field has only the values `0` and `-1`, so it is not a boolean `0/1`.</span>

On a typical two's complement implementation, storing `1` yields `-1`, so `flag == 1` fails. Conversion of an unrepresentable value depends on C's rules and the implementation.[^iso-c-n1570]

For a flag, use `_Bool` (or `bool` from `<stdbool.h>` in C versions before C23) when you need logical `0/1` values; an `unsigned int` bit-field can be used when a one-bit unsigned representation is intended.[^iso-c-n1570]

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
