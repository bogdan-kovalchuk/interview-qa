---
id: emb-fund-0002
title: "What is POSIX?"
description: "POSIX is an IEEE standard defining an API for compatibility between Unix-like operating systems, with subsets implemented even by RTOSes."
track: embedded
section: fundamentals
level: junior
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

**POSIX** (Portable Operating System Interface) is an IEEE standard that defines an API for compatibility between Unix-like operating systems.[^dou-embedded-interview] It describes the file API (`open`/`read`/`write`/`close`), processes (`fork`/`exec`), threads (`pthread`), signals, IPC and regular expressions.

Goal: code written for POSIX compiles and runs on Linux, macOS, FreeBSD and QNX without changes. In Embedded Linux it is the foundation for portability. RTOSes (Zephyr, FreeRTOS) implement POSIX subsets (pthreads, semaphores) for code portability.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
