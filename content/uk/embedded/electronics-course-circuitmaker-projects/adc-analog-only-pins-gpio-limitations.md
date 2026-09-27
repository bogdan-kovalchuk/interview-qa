---
id: emb-elcmproj-0060
title: "Чому виводи ADC6 і ADC7 мікроконтролера ATmega328P не можна використовувати для керування світлодіодами?"
description: "Чому виводи ADC6 і ADC7 мікроконтролера ATmega328P не можна використовувати для керування світлодіодами?"
track: embedded
section: electronics-course-circuitmaker-projects
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 130 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

В архітектурі ATmega328P у корпусі TQFP-32 виводи ADC6 і ADC7 є виключно аналоговими входами мультиплексора. Вони апаратно позбавлені цифрових вихідних транзисторів і регістрів керування портом GPIO. Спроба сконфігурувати їх на вихід не працюватиме, тому світлодіоди підключають до інших ліній.[^udemy-electronics-course]

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
