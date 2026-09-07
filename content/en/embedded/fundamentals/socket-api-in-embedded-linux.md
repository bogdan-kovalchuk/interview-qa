---
id: emb-fund-0015
title: "What is a socket in Linux, and when does an embedded device actually need the socket API?"
description: "A socket is a file descriptor for a network or local-IPC endpoint."
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

**Socket** is a file descriptor for a network or local-IPC endpoint. An embedded device needs the socket API when it speaks TCP/UDP, Unix domain IPC, Bluetooth sockets, or has a daemon/client architecture. For a simple sensor-to-MCU link without an OS, a socket is not needed; there you get UART/SPI/I2C or a lightweight network stack API.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
