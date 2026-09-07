---
id: emb-dtypes-0103
title: "What are hardware registers, and how does a memory-mapped register differ from a CPU general-purpose register?"
description: "A hardware register controls a peripheral or reflects its status; a memory-mapped register is accessed via a volatile pointer at a fixed address, unlike a CPU general-purpose register."
track: embedded
section: data-types-and-memory-layout
level: senior
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
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

A **hardware register** controls a peripheral or reflects its status. A **memory-mapped register** is accessible as an address in the memory map and is typically declared through a `volatile` pointer/struct. A CPU general-purpose register is an internal core register for computation; it is not a peripheral control register.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
