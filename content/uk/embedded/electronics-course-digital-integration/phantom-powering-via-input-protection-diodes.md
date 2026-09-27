---
id: emb-elinteg-0032
title: "Що таке паразитна заживка (phantom powering) через вхідні діоди захисту і чим вона небезпечна?"
description: "Що таке паразитна заживка (phantom powering) через вхідні діоди захисту і чим вона небезпечна?"
track: embedded
section: electronics-course-digital-integration
level: junior
type: pitfall
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 97 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Входи цифрових мікросхем містять внутрішні ESD-діоди захисту, підключені катодами до шини VCC. Якщо подати активний сигнал на вхід незаживленої мікросхеми, струм потече через діод у шину живлення, частково живлячи схему. Це утримує тригери в напівробочому стані, блокує штатне початкове скидання при ввімкненні та може пошкодити вхідний захист.[^udemy-electronics-course]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
