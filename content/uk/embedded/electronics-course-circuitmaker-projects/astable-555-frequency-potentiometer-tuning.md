---
id: emb-elcmproj-0012
title: "Як потенціометри регулюють частоту імпульсів у автоколивальному генераторі на таймері 555?"
description: "Як потенціометри регулюють частоту імпульсів у автоколивальному генераторі на таймері 555?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 113 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Частота генератора задається формулою часу заряду й розряду конденсатора: <span class="formula">\(f \approx 1{,}44 / ((R_A + 2R_B)\,C)\)</span>. Послідовне ввімкнення підлаштовних потенціометрів змінює еквівалентний опір плечей подільника. Це дозволяє плавно підлаштовувати темп спалахів світлодіодів від часток герца до сотень герц.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
