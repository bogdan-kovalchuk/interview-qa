---
id: emb-rtos-0005
title: "What is the difference between a general-purpose OS and a real-time OS?"
description: "GPOS is optimised for throughput and fairness with unpredictable latency, while RTOS targets determinism with bounded latency and low jitter."
track: embedded
section: rtos
level: junior
type: comparison
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
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for rtos concepts; details of specific devices and toolchains can differ."
---

## Short answer

**GPOS** (Linux, Windows): optimised for throughput, fairness, and convenience for many processes; latency can be unpredictable without special real-time configuration.[^dou-embedded-interview]

**RTOS** (FreeRTOS, Zephyr, VxWorks): optimised for **determinism** – bounded latency and predictable worst-case response with properly designed priorities, ISRs, and critical sections. In a preemptive RTOS, a ready task with higher priority preempts a lower one.

Key metric – **jitter** (spread of response time). RTOS task examples: motor control, ABS, medical devices.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
