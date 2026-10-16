---
id: emb-fund-0024
title: "Які framework-и для збірки embedded Linux або kernel ви знаєте: Buildroot, Yocto, OpenWrt, vendor BSP?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

**Buildroot** простіший для генерації rootfs/toolchain/images з fixed configuration. **Yocto** складніший, але гнучкий для продуктів з layers, recipes, package management і довгим lifecycle. **OpenWrt** орієнтований на мережеві пристрої, а vendor BSP часто дає швидкий старт, але може мати застарілий kernel і patches.[^dou-embedded-interview]

## Detailed explanation

TODO
