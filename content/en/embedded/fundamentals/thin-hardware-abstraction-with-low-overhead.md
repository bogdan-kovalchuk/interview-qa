---
id: emb-fund-0021
title: "How do you abstract the hardware layer without excessive runtime overhead?"
description: "Keep the abstraction thin with inline functions, static dispatch, and templates, using function tables only where runtime substitution is needed."
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

Keep the abstraction thin: inline functions, static dispatch, templates in C++, function tables only where runtime substitution is needed. **HAL boundary** should hide register details but must not mask timing, blocking behavior, DMA ownership, or interrupt context. <span class="warn">An overly thick HAL makes the driver unpredictable and hard to debug on an MCU.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
