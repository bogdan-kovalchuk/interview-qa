---
id: emb-fund-0013
title: "How do blocking operations differ from non-blocking operations in drivers and I/O APIs?"
description: "A blocking call sleeps or waits until data or a resource is available, such as read on an empty device queue."
track: embedded
section: fundamentals
level: middle
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

A blocking call sleeps or waits until data or a resource becomes available, for example `read` on an empty device queue. A non-blocking call immediately returns `EAGAIN`/`EWOULDBLOCK` if the operation cannot be performed. In drivers this affects wait queues, poll/select/epoll support, timeouts, and whether the API can be called from a given context.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
