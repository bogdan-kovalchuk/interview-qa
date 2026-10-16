---
id: emb-fund-0024
title: "Which frameworks for building embedded Linux or a kernel do you know: Buildroot, Yocto, OpenWrt, or a vendor BSP?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

**Buildroot** is simpler for generating rootfs/toolchain/images with fixed configuration. **Yocto** is more complex but flexible for products with layers, recipes, package management, and a long lifecycle. **OpenWrt** targets network devices, and a vendor BSP often gives a quick start but may ship with an outdated kernel and patches.[^dou-embedded-interview]

## Detailed explanation

TODO
