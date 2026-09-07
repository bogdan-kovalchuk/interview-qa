---
id: emb-boot-0007
title: "Що таке OTA update і які ризики треба закрити: power loss, signature verification, rollback і version compatibility?"
description: "OTA - оновлення firmware через мережу без фізичного доступу. Потрібні atomic install, image integrity, signature verification, anti-rollback policy, version compatibility з config/protocol і recovery після power loss."
track: embedded
section: bootloaders-and-ota
level: senior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
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

**OTA** - оновлення firmware через мережу без фізичного доступу до пристрою. Потрібні atomic install, image integrity, signature verification, anti-rollback policy, version compatibility з config/protocol і recovery після power loss. <span class="warn">Без rollback або safe boot OTA може перетворити remote device на недоступний brick.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
