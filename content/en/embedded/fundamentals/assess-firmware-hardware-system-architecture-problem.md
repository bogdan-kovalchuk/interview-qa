---
id: emb-fund-0028
title: "How to assess whether a problem should be solved by firmware, hardware design, or system architecture?"
description: "Identify the symptom, constraint and failure mode, then decide whether firmware, hardware or system architecture should solve it based on responsibility boundaries."
track: embedded
section: fundamentals
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for fundamentals concepts; details of specific devices and toolchains can differ."
---

## Short answer

First identify the symptom, constraint and failure mode: timing, noise margin, resource limit, protocol mismatch or requirement gap. Firmware suits sequencing, filtering, diagnostics and policy; hardware – signal integrity, protection, analog limits and deterministic safety cutoff. **System architecture** is needed when the problem arises from a wrong distribution of responsibility between blocks or impossible requirements.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
