---
id: emb-fund-0020
title: "How do you maintain one codebase for different MCUs, boards, and peripheral configurations?"
description: "Separate a portable core, MCU-specific drivers, board support package, and configuration data, describing hardware differences through build options rather than scattered ifdefs."
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

Separate a **portable core**, MCU-specific drivers, board support package, and configuration data. Describe hardware differences through target-specific build options, linker scripts, pin/clock tables, and devicetree-like configuration rather than chaotic `#ifdef` scattered through the logic. CI should build key variants so divergence is caught early.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
