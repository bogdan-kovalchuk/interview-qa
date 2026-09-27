---
id: emb-elcmproj-0062
title: "Навіщо між виводом ШІМ мікроконтролера та аудіопідсилювачем встановлюють фільтр низьких частот?"
description: "Навіщо між виводом ШІМ мікроконтролера та аудіопідсилювачем встановлюють фільтр низьких частот?"
track: embedded
section: electronics-course-circuitmaker-projects
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 131 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Прямокутний сигнал ШІМ містить високочастотну несучу складову, яка викликає шуми та перегрів підсилювача. Пасивний фільтр RC із частотою зрізу <span class="formula">\(f_c = 1 / (2\pi R C)\)</span> згладжує імпульси, виділяючи звукову хвилю. На вхід підсилювача надходить відновлений аналоговий сигнал без паразитних високочастотних гармонік.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
