---
id: emb-fund-0003
title: "What is a system call?"
description: "A system call switches the CPU from user space to kernel mode via a call number in a register to obtain a kernel service with memory isolation."
track: embedded
section: fundamentals
level: junior
type: mechanism
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

**System call (syscall)** is a mechanism for requesting kernel services from user space.[^dou-embedded-interview] Since user space has no direct access to hardware and kernel resources, a program issues a syscall to switch into kernel mode.

Mechanism (x86-64): the program places the syscall number in `rax`, arguments in `rdi/rsi/rdx...`, and executes the `syscall` instruction. The kernel switches to privileged mode, runs the handler, and returns the result.

It provides isolation: user-space processes cannot corrupt kernel memory or the memory of other processes.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
