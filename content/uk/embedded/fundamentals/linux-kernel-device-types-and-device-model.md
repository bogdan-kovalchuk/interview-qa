---
id: emb-fund-0022
title: "Які типи пристроїв існують у Linux kernel і як вони представлені через device model?"
description: "У Linux є character, block, network, platform, bus-specific devices тощо.Device model представляє їх через struct device, bus, driver, class і sysfs n…"
track: embedded
section: fundamentals
level: senior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу fundamentals; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

У Linux є **character**, **block**, **network**, platform, bus-specific devices тощо. Device model представляє їх через `struct device`, bus, driver, class і sysfs nodes. Для embedded важливі platform devices, devicetree/ACPI опис hardware і binding driver до compatible/resource data.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
