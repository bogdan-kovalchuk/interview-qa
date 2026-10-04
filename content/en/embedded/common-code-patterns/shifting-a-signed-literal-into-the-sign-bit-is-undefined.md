---
id: emb-patterns-0015
title: "Trap: why do bit shifts need an unsigned literal rather than `1`?"
description: "1 31 is undefined behavior because the literal 1 is a signed int and shifting into the sign bit overflows it"
track: embedded
section: common-code-patterns
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

## Short answer

<span class="warn">`1 << 31` is undefined behavior</span>: the literal `1` has type signed `int`, and the result is not representable as `int` on a platform with 32-bit `int`.[^iso-c-n1570]

`1U << 31` is valid only if the left operand's type after integer promotions has at least 32 bits; otherwise the shift count is too large.[^iso-c-n1570]

For 32-bit masks, use `UINT32_C(1) << n` and ensure `n < 32`; for other widths, choose an unsigned type of suitable width and check its limits.[^iso-c-n1570]

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
