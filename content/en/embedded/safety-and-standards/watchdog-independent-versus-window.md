---
id: emb-safety-0001
title: "What watchdog functions exist, and how does an independent watchdog differ from a window watchdog?"
description: "An independent watchdog uses a separate clock, while a window watchdog detects refreshes that are too early as well as too late."
track: embedded
section: safety-and-standards
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
  - source_id: iec-61508-1-2010
    title: "IEC 61508-1:2010 ? Functional safety: General requirements"
    url: https://webstore.iec.ch/en/publication/5515
    accessed: 2026-09-06
    kind: spec
    version: "IEC 61508-1:2010"
    applicability: "Authoritative section-level reference for safety and standards concepts; details of specific devices and toolchains can differ."
---

## Short answer

A watchdog resets the system if firmware does not perform a refresh in time. **Independent watchdog** typically has a separate low-speed clock and works even during main clock problems. **Window watchdog** requires a refresh neither too early nor too late, so it catches both hangs and runaway loops.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
