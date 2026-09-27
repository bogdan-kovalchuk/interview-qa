---
id: emb-elinteg-0039
title: "Як здійснюється керування напрямком і станом шини в двонапрямленому трансивері 74x245?"
description: "Як здійснюється керування напрямком і станом шини в двонапрямленому трансивері 74x245?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 98 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Мікросхема 74x245 містить зустрічно-паралельні пари тристабільних буферів для кожної з 8 ліній шини. Вхід DIR задає напрямок передачі: при DIR = 1 дані передаються з порту A на порт B, а при DIR = 0 – з B на A. За високого рівня на вході дозволу <span class="formula">\(\overline{OE}=1\)</span> обидва порти ізолюються та переходять у стан високого імпедансу Hi-Z.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
