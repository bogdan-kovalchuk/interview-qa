---
id: emb-fund-0022
title: "Which device types exist in the Linux kernel, and how are they represented by the device model?"
description: "Linux has character, block, network, platform, and bus-specific devices represented through struct device, bus, driver, class, and sysfs nodes."
track: embedded
section: fundamentals
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
    applicability: "Authoritative section-level reference for fundamentals concepts; details of specific devices and toolchains can differ."
---

## Short answer

Linux has **character**, **block**, **network**, platform, and bus-specific devices, among others. The device model represents them through `struct device`, bus, driver, class, and sysfs nodes. For embedded, platform devices, devicetree/ACPI hardware description, and driver binding to compatible/resource data are important.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
