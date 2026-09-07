---
id: emb-fund-0014
title: "Which IPC mechanisms are appropriate in Embedded Linux, and what are the trade-offs of pipes, sockets, shared memory, and message queues?"
description: "A pipe is simple for a stream between related processes but is local and one-way."
track: embedded
section: fundamentals
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for fundamentals concepts; details of specific devices and toolchains can differ."
---

## Short answer

`pipe` is simple for a stream between related processes, but local and one-way. `socket` is flexible: Unix domain for local IPC or TCP/UDP for network, but has overhead. `shared memory` is fastest for large data but requires synchronization; `message queue` provides message boundaries and priority, but is limited in size by system limits.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
