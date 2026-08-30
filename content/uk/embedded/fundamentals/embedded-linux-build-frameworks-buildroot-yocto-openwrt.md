---
id: emb-fund-0024
title: "Які framework-и для збірки embedded Linux або kernel ви знаєте: Buildroot, Yocto, OpenWrt, vendor BSP?"
description: "Buildroot, Yocto, OpenWrt і vendor BSP мають різний баланс простоти, гнучкості, package management та lifecycle."
track: embedded
section: fundamentals
level: senior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
---

## Short answer

<span class="key">Buildroot</span> простіший для генерації rootfs/toolchain/images з fixed configuration.<br><span class="key">Yocto</span> складніший, але гнучкий для продуктів з layers, recipes, package management і довгим lifecycle.<br><span class="key">OpenWrt</span> орієнтований на мережеві пристрої, а vendor BSP часто дає швидкий старт, але може мати застарілий kernel і patches.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
