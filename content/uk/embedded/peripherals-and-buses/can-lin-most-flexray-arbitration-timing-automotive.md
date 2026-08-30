---
id: emb-periph-0019
title: "Як працюють CAN, LIN, MOST і FlexRay, і чим вони відрізняються за arbitration, timing і automotive use-case?"
description: "CAN має multi-master arbitration за message ID, LIN дешевший master-slave bus, FlexRay дає deterministic time-triggered communication, MOST історично для automotive multimedia."
track: embedded
section: peripherals-and-buses
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
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? peripherals-and-buses; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<span class="key">CAN</span> має multi-master arbitration за message ID і добре підходить для robust control networks.<br><span class="key">LIN</span> дешевший master-slave bus для простих actuators/sensors; <span class="key">FlexRay</span> дає deterministic time-triggered communication для safety-critical systems.<br><span class="key">MOST</span> історично використовувався для automotive multimedia; його роль інша, ніж у control buses.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
