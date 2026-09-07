---
id: emb-debug-0003
title: "How do you use an oscilloscope or logic analyzer to check UART, SPI, I2C, and timing issues?"
description: "An oscilloscope reveals electrical and timing quality, while a logic analyzer decodes bus transactions and links them to firmware markers."
track: embedded
section: debugging-and-tracing
level: middle
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

Use an oscilloscope to check voltage levels, edges, ringing, rise/fall time, clock, and reset/power timing. A logic analyzer decodes UART/SPI/I2C frames, showing baud/clock, ACK/NACK, CS timing, and gaps between bytes. Best practice is to trigger on the problem event and simultaneously watch a firmware GPIO marker to link the code path with the signal.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

