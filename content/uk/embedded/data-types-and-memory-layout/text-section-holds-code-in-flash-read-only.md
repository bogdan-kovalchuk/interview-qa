---
id: emb-dtypes-0001
title: "Що таке секція `.text` у пам'яті embedded програми?"
description: "Секція .text зберігає скомпільований код і на embedded лежить у Flash як read-only."
track: embedded
section: data-types-and-memory-layout
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

Секція **.text** містить скомпільований машинний код (інструкції) усіх функцій програми. У embedded вона зберігається у **Flash-пам'яті** та є read-only.

CPU виконує інструкції безпосередньо з Flash (XIP - Execute in Place) або після копіювання у RAM для підвищення швидкості. Спроба запису у `.text` -> HardFault (якщо MPU налаштований).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
