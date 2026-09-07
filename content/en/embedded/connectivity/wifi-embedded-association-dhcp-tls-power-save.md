---
id: emb-conn-0007
title: "How does Wi-Fi work on an embedded device and what are the implications of association, DHCP, TLS, and power save modes?"
description: "Embedded Wi-Fi associates with an AP, gets an IP via DHCP, pays CPU and RAM for TLS handshakes and certificates, and trades power save for added latency and harder reconnect paths."
track: embedded
section: connectivity
level: senior
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
    applicability: "Authoritative section-level reference for connectivity concepts; details of specific devices and toolchains can differ."
---

## Short answer

Embedded Wi-Fi goes through scan/auth/association with an AP, then obtains an IP via DHCP or static config. TLS adds CPU/RAM cost, certificates, entropy and long handshakes, which matters for a small MCU. Power save modes reduce consumption but add latency, buffering at the AP, and more complex reconnect/error paths.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
