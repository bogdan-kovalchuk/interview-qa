---
id: emb-cemb-0039
title: "Why do C99 and C11 matter for embedded C, and which C11 features may be unavailable in MCU toolchains?"
description: "C99 and C11 added useful embedded features, but C11 support must be checked for the actual MCU toolchain."
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

C99 brought `stdint.h`, `stdbool.h`, designated initializers, mixed declarations, and `inline`, which are very useful for embedded. C11 added atomics, threads, alignment features, and static assertions. <span class="warn">On MCU toolchains C11 threads/atomics may be incomplete or depend on the runtime/libc</span>, so the specific compiler and flags must be checked.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
