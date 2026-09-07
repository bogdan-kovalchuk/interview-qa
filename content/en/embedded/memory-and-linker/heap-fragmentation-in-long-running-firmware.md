---
id: emb-memlink-0013
title: "What is heap fragmentation, and how does it appear in long-running firmware?"
description: "Heap fragmentation can cause allocation failures even when total free memory appears sufficient."
track: embedded
section: memory-and-linker
level: middle
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
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "Authoritative section-level reference for memory and linker concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Heap fragmentation** is a situation where there is enough total free memory, but it is split into small non-contiguous blocks. In firmware this appears as random `malloc` failures after hours or days of operation, especially with varying allocation sizes. Typical countermeasures: fixed-size pools, allocate-on-startup, bounded lifetimes and no heap in ISR.[^dou-embedded-interview]

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
