---
id: emb-fund-0024
title: "Which frameworks for building embedded Linux or a kernel do you know: Buildroot, Yocto, OpenWrt, or a vendor BSP?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: buildroot-manual
    title: "The Buildroot user manual"
    url: https://buildroot.org/downloads/manual/manual.html
  - source_id: yocto-overview-intro
    title: "Yocto Project Overview and Concepts Manual: Introducing the Yocto Project"
    url: https://docs.yoctoproject.org/overview-manual/yp-intro.html
  - source_id: openwrt-readme
    title: "OpenWrt source repository README"
    url: https://github.com/openwrt/openwrt/blob/main/README.md
---

## Short answer

**Buildroot** is simpler for generating rootfs/toolchain/images with fixed configuration. **Yocto** is more complex but flexible for products with layers, recipes, package management, and a long lifecycle. **OpenWrt** targets network devices, and a vendor BSP often gives a quick start but may ship with an outdated kernel and patches.[^dou-embedded-interview]

## Detailed explanation

TODO
