---
id: emb-elcmproj-0042
title: "Чому паралельно до котушки динаміка в однотактному підсилювачі обов’язково вмикають діод?"
description: "Чому паралельно до котушки динаміка в однотактному підсилювачі обов’язково вмикають діод?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 123 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Котушка динаміка володіє індуктивністю, яка при різкому закриванні транзистора створює зворотний викид напруги: <span class="formula">\(v_L = L\,(di/dt)\)</span>. Високовольтний індуктивний сплеск перевищує допустиму межу <span class="formula">\(V_{CEO}\)</span> транзистора й пробиває перехід. Зворотний діод безпечно закорочує струм котушки на себе, захищаючи кристал.[^udemy-electronics-course]

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
