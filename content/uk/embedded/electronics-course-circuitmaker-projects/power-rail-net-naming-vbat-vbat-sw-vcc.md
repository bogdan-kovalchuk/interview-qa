---
id: emb-elcmproj-0039
title: "Навіщо ланцюгам живлення батарейного пристрою дають різні імена VBAT, VBAT_SW і VCC?"
description: "Навіщо ланцюгам живлення батарейного пристрою дають різні імена VBAT, VBAT_SW і VCC?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 122 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Роздільні назви ланцюгів запобігають випадковому помилковому об’єднанню ділянок живлення в один провідний netlist. Позначення VBAT належить прямим виводам батареї, VBAT_SW – колу після вимикача, а VCC – виходу стабілізатора напруги. Це ізолює вузли комутації й гарантує коректне трасування провідників.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
