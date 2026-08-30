---
id: emb-boot-0001
title: "Що таке device tree?"
description: "Device Tree описує апаратуру плати окремо від коду ядра; bootloader компілює .dts у .dtb і передає його адресу ядру Linux при завантаженні."
track: embedded
section: bootloaders-and-ota
level: junior
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

**Device Tree** – структура даних, що описує апаратуру плати (CPU, пам'ять, периферія, переривання, шини) у вигляді, не залежному від коду ядра.[^dou-embedded-interview] Дозволяє одному образу ядра Linux підтримувати різні плати.

Файли: `.dts` (Device Tree Source, текст) компілюється `dtc` у `.dtb` (Device Tree Blob, бінарний файл). Bootloader (U-Boot) передає адресу DTB ядру при завантаженні.

Приклад вузла: описує UART1 – базову адресу регістрів, номер переривання, тактування. Драйвер у ядрі читає ці параметри через DT API.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
