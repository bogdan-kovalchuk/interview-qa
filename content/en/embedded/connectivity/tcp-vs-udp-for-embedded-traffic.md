---
id: emb-conn-0004
title: "How does TCP differ from UDP for telemetry, control commands, and firmware updates?"
description: "TCP provides an ordered reliable stream, while UDP provides lower-overhead datagrams whose reliability must be added when required."
track: embedded
section: connectivity
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for connectivity concepts; details of specific devices and toolchains can differ."
---

## Short answer

TCP provides an ordered reliable byte stream with retransmission and flow control, making it suitable for firmware updates or commands where integrity matters. UDP provides datagrams with no delivery or ordering guarantee, but lower overhead and latency, useful for frequent telemetry samples or real-time data. If UDP is used for a critical command or update, reliability, ordering and authentication must be built on top.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

