---
id: emb-elinteg-0073
title: "Як безпечно об'єднати тактовий генератор і кнопку ручного тактування для керування лічильником?"
description: "Як безпечно об'єднати тактовий генератор і кнопку ручного тактування для керування лічильником?"
track: embedded
section: electronics-course-digital-integration
level: junior
type: concept
tags: []
status: published
updated: 2026-09-27
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 106 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Виходи генератора імпульсів і кнопки з підтяжкою не можна з'єднувати паралельно через виникнення струмового конфлікту шини при незбігу рівнів. Їх підключають через двовходовий логічний елемент OR, вихід якого надходить на тактовий вхід лічильника. Під час ручного тактування генератор необхідно зупинити або перевести в стан логічного 0, інакше постійна одиниця на вході OR заблокує сигнали від кнопки.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
