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

## Short answer

<span class="warn">`1 << 31` is undefined behavior</span>: the literal `1` has type signed `int`, and shifting into the sign bit overflows it.

`1U << 31` is defined only if `unsigned int` is wider than 31 bits. On a 16-bit `unsigned int` it is also incorrect because the shift count is too large.

Defense: for 32-bit masks write `UINT32_C(1) << n`; for register-width masks pick a literal of the appropriate width.[^embeddedinterviewlab]

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
