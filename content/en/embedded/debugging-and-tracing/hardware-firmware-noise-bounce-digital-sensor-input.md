---
id: emb-debug-0005
title: "What simple hardware and firmware methods remove noise/bounce on a digital sensor input?"
description: "Hardware methods include pull resistors, RC filters, Schmitt triggers, and shielding; firmware uses debounce timers, majority vote, and interrupt masking."
track: embedded
section: debugging-and-tracing
level: senior
type: concept
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

Hardware: pull-up/pull-down of the correct value, RC filter, Schmitt trigger, shielding/grounding, series resistor, or opto/isolator where needed. Firmware: debounce timer, majority vote, state machine with stable time, interrupt masking over the debounce window. <span class="warn">Do not mask a wiring/grounding problem with a firmware filter if the noise can damage the input or cause a safety event.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
