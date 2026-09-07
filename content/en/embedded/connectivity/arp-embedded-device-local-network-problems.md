---
id: emb-conn-0008
title: "What is ARP and when does an embedded device actually encounter ARP problems in a local network?"
description: "ARP maps IPv4 to MAC on a local segment; embedded devices hit ARP issues at first connect, on IP conflict, stale cache, link flap, or sleep/wake, with symptoms like lost first packets and failed LAN pings."
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

**ARP** maps an IPv4 address to a MAC address within a local Ethernet/Wi-Fi segment. An embedded device encounters ARP at the first connect to a gateway/peer, on IP conflict, stale ARP cache, link flap, or sleep/wake scenarios. Symptoms: ping fails within the LAN, the first packet is lost, and after an IP/MAC change a gratuitous ARP is needed.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
