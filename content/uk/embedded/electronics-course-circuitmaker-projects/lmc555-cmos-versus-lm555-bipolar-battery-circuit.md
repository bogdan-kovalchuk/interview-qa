---
id: emb-elcmproj-0011
title: "Чому для батарейних пристроїв обирають КМОН-таймер LMC555 замість класичного біполярного LM555?"
description: "Чому для батарейних пристроїв обирають КМОН-таймер LMC555 замість класичного біполярного LM555?"
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

КМОН-таймер LMC555 зберігає працездатність за низької напруги від <span class="formula">\(1{,}5\ \text{В}\)</span> і споживає частки міліампера струму. Він позбавлений наскрізних струмових викидів під час перемикання внутрішніх транзисторів вихідного каскаду. Це захищає шину живлення від високочастотних шумів і продовжує ресурс батарейного живлення.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
