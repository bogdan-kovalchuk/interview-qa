---
id: emb-fund-0027
title: "Linux controller cannot start new processes even though df shows free space. How to check inodes, tmpfs, file descriptors, and logs?"
description: "Check inodes with df -i, tmpfs with df -h, file descriptors with ulimit and lsof, and review dmesg and journalctl for OOM, read-only remount or filesystem errors."
track: embedded
section: fundamentals
level: senior
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for fundamentals concepts; details of specific devices and toolchains can differ."
---

## Short answer

Check `df -i` for inodes, `df -h` for `/tmp`/`/run` tmpfs, `ulimit -n` and `lsof` for file descriptors. Look at `dmesg`, `journalctl`, OOM messages, read-only remount and filesystem errors. <span class="warn">Free bytes on rootfs won't help if inodes, PID limit, fd limit or tmpfs are exhausted.</span>[^dou-embedded-interview]

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
