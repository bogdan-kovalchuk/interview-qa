---
id: emb-macros-0044
title: "Trap: what is wrong with `#define BIT(n) (1 << (n))` at `BIT(31)`?"
description: "On a platform with 32-bit int, 1 << 31 has no defined result; unsigned shifts also require a count within the operand width."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

On a platform with 32-bit `int`, the literal `1` has type `int`, and `1 << 31` has undefined behavior because the power of two is not representable in the signed result type.[^iso-c-n1570]

On many MCUs it "works" as `0x80000000`, but the standard does not guarantee this, and the compiler may optimize unpredictably.

For an unsigned shift, the result is reduced modulo the type's range, but `n` must still be less than the width of the promoted left operand. For a fixed 32-bit mask, use `UINT32_C(1)` and check `n < 32`.[^iso-c-n1570]

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
