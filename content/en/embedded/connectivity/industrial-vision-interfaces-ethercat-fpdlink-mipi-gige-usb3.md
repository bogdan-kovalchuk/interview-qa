---
id: emb-conn-0013
title: "Which industrial or vision interfaces can be embedded-relevant but niche: EtherCAT, FPD-Link III, MIPI CSI, GigE Vision, USB3 Vision?"
description: "EtherCAT is deterministic industrial Ethernet for motion, FPD-Link III and MIPI CSI handle camera/display pipelines on SoCs, and GigE Vision and USB3 Vision are machine-vision transports."
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

**EtherCAT** is deterministic industrial Ethernet for motion/control, often with a dedicated slave controller. **FPD-Link III** and **MIPI CSI** appear frequently in camera/display pipelines on embedded SoC. **GigE Vision** and **USB3 Vision** are machine-vision transports where bandwidth, latency, drivers and buffer handling matter.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
