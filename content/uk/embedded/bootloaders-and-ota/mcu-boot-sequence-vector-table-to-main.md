---
id: emb-boot-0003
title: "Як відбувається завантаження програми в мікроконтролері?"
description: "Після reset Cortex-M читає vector table, вантажить SP і Reset Handler, startup code копіює .data й обнуляє .bss, тактування ініціалізується, і викликається main()."
track: embedded
section: bootloaders-and-ota
level: junior
type: mechanism
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
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "Авторитетне джерело рівня секції для понять розділу bootloaders-and-ota; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Після подачі живлення або reset (ARM Cortex-M):[^dou-embedded-interview]

- Апаратура читає **Vector Table** з адреси `0x00000000` (Flash)
- Завантажує початкове значення SP зі слова за адресою `0x00000000`
- Завантажує адресу Reset Handler у PC з `0x00000004`
- **Startup code** (crt0 / startup.s) копіює секцію `.data` з Flash у RAM, заповнює `.bss` нулями
- Ініціалізує тактування (PLL, clock tree)
- Викликає `main()`.

Програма зберігається у **Flash (non-volatile)**, виконується звідти або копіюється в RAM (XIP або execute-in-place).

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
