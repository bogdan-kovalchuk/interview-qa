---
id: emb-rtos-0004
title: "What is a deadlock?"
description: "Deadlock occurs when two or more threads mutually wait for each other's resources; fixed lock order and timeout prevent it."
track: embedded
section: rtos
level: junior
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
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for rtos concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Deadlock** is a situation where two or more threads mutually wait for each other's resources and none can proceed.[^dou-embedded-interview]

Example: Thread A took `m1` and waits for `m2`, while Thread B took `m2` and waits for `m1`. Both are blocked forever.

Prevention: fixed order of acquiring locks, short critical sections, timeout, lock hierarchy, avoiding nested locks, or using higher-level primitives.

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
