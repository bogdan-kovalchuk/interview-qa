---
id: emb-fund-0004
title: "What is a file descriptor?"
description: "A file descriptor is a non-negative integer the kernel uses to identify an open process resource: file, socket, pipe, or device."
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

**File descriptor (fd)** is a non-negative integer that identifies an open resource within a process: file, socket, pipe, or device.[^dou-embedded-interview] The kernel maintains an fd table for each process.

Standard ones: `0` = stdin, `1` = stdout, `2` = stderr.

Cycle: `fd = open("file", O_RDONLY);`, then `read(fd, buf, n);`, then `close(fd);`. In Linux "everything is a file" – through an fd you can work with devices (`/dev/gpio`), sysfs, and even timers (`timerfd`).

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
