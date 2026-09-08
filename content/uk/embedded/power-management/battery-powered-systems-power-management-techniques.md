---
id: emb-power-0001
title: "Які типові методи керування живленням використовуються в embedded-системах з батарейним живленням?"
description: "Системи з батарейним живленням знижують середнє споживання через duty cycling, доречні sleep states, clock чи power gating та керування частотою або напругою, якщо це підтримує hardware."
track: embedded
section: power-management
level: middle
type: concept
tags: []
status: published
updated: 2026-09-08
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: arm-cortex-m-low-power
    title: "ARM: Cortex-M Low Power Design"
    url: https://developer.arm.com/documentation/102499/0100/
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Офіційна документація ARM про низькоспоживчий дизайн для Cortex-M."
---

## Short answer

**Знижуйте середнє споживання через duty cycling: групуйте корисну роботу, прокидайтеся за потрібною подією або таймером і повертайтеся у доречний sleep state.** Вимикайте тактування невикористаної периферії, застосовуйте power gating, якщо його підтримує hardware, а частоту й напругу знижуйте лише в дозволених operating points.[^arm-cortex-m-low-power] Час роботи radio та sensor, quiescent current регуляторів і leakage можуть бути важливішими за час CPU. Найглибший sleep state не завжди найкращий: враховуйте енергію й latency пробудження, retention state, запуск clock і real-time deadlines.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
