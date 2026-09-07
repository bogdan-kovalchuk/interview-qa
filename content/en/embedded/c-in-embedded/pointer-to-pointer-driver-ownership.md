---
id: emb-cemb-0038
title: "Why are pointer-to-pointers used in drivers, resource APIs, and linked structures?"
description: "A pointer-to-pointer lets an API change the caller's pointer, return a handle, or update a list head or tail."
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

`T **` is needed when a function must change the caller's pointer: to issue a handle, add a node at the list head, or return a buffer from a pool. In drivers this often looks like `driver_open(dev_t **out)` or a queue API that updates head/tail. It is important to document ownership: who frees or returns the resource afterward.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
