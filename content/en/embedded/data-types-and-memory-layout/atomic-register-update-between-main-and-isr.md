---
id: emb-dtypes-0104
title: "How do you ensure an atomic register update when both main code and an ISR modify one register?"
description: "Use set/clear aliases or a critical section to make register updates atomic; an unprotected read-modify-write can lose a bit changed by an ISR."
track: embedded
section: data-types-and-memory-layout
level: senior
type: pitfall
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
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

If the register has set/clear/toggle aliases or bit-banding, use them instead of read-modify-write. Otherwise, protect with a critical section: temporarily disable the relevant interrupt or use an atomic primitive if the architecture supports it. <span class="warn">An unprotected read-modify-write can lose a bit changed by an ISR between the read and the write.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
