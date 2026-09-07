---
id: emb-debug-0004
title: "Oscilloscope shows a glitch on a sensor 0-1 transition. How to distinguish bounce, EMI, ground issue, and sampling problem?"
description: "Bounce is repetitive and tied to a mechanical edge; EMI correlates with switching events; ground issues shift the reference; sampling problems show aliasing."
track: embedded
section: debugging-and-tracing
level: senior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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
  - source_id: gdb-manual
    title: "Debugging with GDB"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.pdf
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "Authoritative section-level reference for debugging and tracing concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Bounce** is usually repetitive and tied to a mechanical edge; EMI may correlate with motor/PWM/radio events. A ground issue shows up as a reference shift, ringing between ground points, or a change with different probe grounding. A sampling problem appears when the analog signal is normal but the firmware catches alias/metastability due to a wrong threshold, debounce, or sample rate.[^dou-embedded-interview]

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
