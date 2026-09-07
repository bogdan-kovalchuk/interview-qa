---
id: emb-fund-0001
title: "What system calls do you know?"
description: "System calls are grouped into categories: file system, processes, memory, network, synchronisation and devices."
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

Main categories:[^dou-embedded-interview]

- **File system**: `open()`, `read()`, `write()`, `close()`, `lseek()`, `stat()`, `unlink()`
- **Processes**: `fork()`, `exec()`, `wait()`, `exit()`, `getpid()`
- **Memory**: `mmap()`, `munmap()`, `brk()`
- **Network**: `socket()`, `bind()`, `connect()`, `send()`, `recv()`
- **Synchronisation**: `futex()`
- **Devices**: `ioctl()`.

Browse them all: `man 2 syscalls` or the file `arch/x86/entry/syscalls/syscall_64.tbl` in the kernel source.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
