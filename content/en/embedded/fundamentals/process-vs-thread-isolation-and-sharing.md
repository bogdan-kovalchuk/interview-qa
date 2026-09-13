---
id: emb-fund-0006
title: "What is the difference between a process and a thread?"
description: "A process has its own address space and is isolated from others, while threads of one process share memory but require synchronization."
track: embedded
section: fundamentals
level: junior
type: comparison
tags: []
status: published
updated: 2026-09-13
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

**Process** is a separate running program with its own address space, OS resources, file descriptor table and at least one thread.[^dou-embedded-interview] Processes are isolated: a fault in one usually does not corrupt another's memory.

**Thread** is a unit of execution inside a process; threads share memory, heap, globals and descriptors, but each has its own stack, registers and instruction pointer.

Consequence: processes isolate more safely but cost more to create and need IPC; threads are lighter and share data faster, yet need synchronization (`mutex`, `semaphore`, `atomic`) against race conditions.
## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
