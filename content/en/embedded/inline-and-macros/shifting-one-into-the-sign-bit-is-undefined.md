---
id: emb-macros-0044
title: "Trap: what is wrong with `#define BIT(n) (1 << (n))` at `BIT(31)`?"
description: "The literal 1 is signed int, so 1 31 shifts into the sign bit, which is undefined behavior on a 32-bit signed int."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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

<span class="warn">The literal `1` has type `int`</span> (signed), so `1 << 31` shifts a bit into the sign position -> <span class="warn">undefined behavior</span> for signed on a 32-bit `int`.

On many MCUs it "works" as `0x80000000`, but the standard does not guarantee this, and the compiler may optimize unpredictably.

Fix: `#define BIT(n) (1u << (n))` or `(UINT32_C(1) << (n))` – unsigned shift is defined.[^embeddedinterviewlab]

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
