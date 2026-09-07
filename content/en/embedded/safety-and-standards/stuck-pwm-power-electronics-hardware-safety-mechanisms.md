---
id: emb-safety-0003
title: "Why can a stuck PWM in power electronics be dangerous for hardware and what safety mechanisms should be built in?"
description: "A stuck PWM can leave power switches in a dangerous state, so hardware shutdown, dead-time, current and temperature limits, and watchdog are required."
track: embedded
section: safety-and-standards
level: senior
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
  - source_id: iec-61508-1-2010
    title: "IEC 61508-1:2010 ? Functional safety: General requirements"
    url: https://webstore.iec.ch/en/publication/5515
    accessed: 2026-09-06
    kind: spec
    version: "IEC 61508-1:2010"
    applicability: "Authoritative section-level reference for safety and standards concepts; details of specific devices and toolchains can differ."
---

## Short answer

A stuck PWM can leave a MOSFET or IGBT in a dangerous duty or open both legs simultaneously, leading to shoot-through, overheating, or load destruction. Required measures: hardware shutdown, dead-time, current and temperature limits, watchdog, timer fault inputs, and safe default state of pins. <span class="warn">Safety must not rely only on the main loop; the critical shutdown mechanism must work even during a firmware hang.</span>[^dou-embedded-interview]

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
