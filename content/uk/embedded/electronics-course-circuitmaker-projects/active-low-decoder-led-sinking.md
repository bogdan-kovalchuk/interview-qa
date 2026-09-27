---
id: emb-elcmproj-0005
title: "Чому катоди світлодіодів підключають до виходів дешифратора 74HC138, а аноди до живлення?"
description: "Чому катоди світлодіодів підключають до виходів дешифратора 74HC138, а аноди до живлення?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 111 курсу на Udemy."
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
    accessed: 2026-09-27
    kind: official
    version: null
    applicability: "Авторитетне джерело рівня секції: основи друкованих плат і робота в CircuitMaker; конкретні проєкти курсу можуть відрізнятися."
---

## Short answer

Дешифратор 74HC138 має інверсні виходи з активним низьким рівнем напруги. При виборі адреси канал переходить у нуль і замикає втікаючий струм світлодіода на землю. Підключення анодів через резистори до шини живлення вмикає вибраний світлодіод саме при появі нуля.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
