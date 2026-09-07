---
id: emb-fund-0017
title: "How does Harvard architecture differ from von Neumann, and how does this affect Flash/RAM access?"
description: "Harvard architecture separates instruction and data memories or buses, changing how firmware accesses Flash and RAM."
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

In **von Neumann**, code and data share one address space/bus. In **Harvard**, instruction and data memories/buses are separate, so Flash and RAM can have different access rules. On some MCUs, reading constants from program memory requires special instructions/API, and self-programming Flash has erase/write and timing limitations.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

