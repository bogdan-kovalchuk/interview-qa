---
id: emb-cemb-0043
title: "How are function parameters passed under EABI on ARM Cortex-M?"
description: "Under ARM EABI, simple integer and pointer arguments use r0–r3, while additional or large aggregate arguments go through the stack."
track: embedded
section: c-in-embedded
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

Under ARM EABI/AAPCS the first simple integer/pointer arguments are typically passed in `r0-r3`, and the result in `r0` or `r0:r1`. Additional arguments and parts of large aggregate objects go through the stack with proper alignment. Registers `r4-r11` are callee-saved, and `r0-r3,r12,lr` are caller-saved in the normal calling convention.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
