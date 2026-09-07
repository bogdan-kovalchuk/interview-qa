---
id: emb-fund-0024
title: "Which frameworks for building embedded Linux or a kernel do you know: Buildroot, Yocto, OpenWrt, or a vendor BSP?"
description: "Buildroot, Yocto, OpenWrt, and vendor BSPs trade off simplicity, flexibility, package management, and lifecycle support."
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

**Buildroot** is simpler for generating rootfs/toolchain/images with fixed configuration. **Yocto** is more complex but flexible for products with layers, recipes, package management, and a long lifecycle. **OpenWrt** targets network devices, and a vendor BSP often gives a quick start but may ship with an outdated kernel and patches.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
