---
id: emb-conn-0010
title: "What is an Ethernet frame and which fields matter when working with raw Ethernet, AVB, or industrial Ethernet?"
description: "An Ethernet frame carries MAC addresses, EtherType, payload and FCS with an optional VLAN tag; raw Ethernet needs MAC filtering, MTU and padding, while AVB and industrial Ethernet add timestamping, QoS and deterministic latency."
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

An **Ethernet frame** contains destination/source MAC, EtherType or length, payload and FCS; a VLAN tag can add priority/VID. For raw Ethernet, MAC filtering, MTU, padding and EtherType matter. For AVB/industrial Ethernet, timestamping, priority/QoS, deterministic latency and MAC/PHY/driver interaction are critical.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
