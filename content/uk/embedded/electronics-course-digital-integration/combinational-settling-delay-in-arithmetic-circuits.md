---
id: emb-elinteg-0042
title: "Чому тактову частоту системи слід обмежувати з урахуванням затримки комбінаційного компаратора?"
description: "Чому тактову частоту системи слід обмежувати з урахуванням затримки комбінаційного компаратора?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 99 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Компаратор є чисто комбінаційною схемою, вихід якої стабілізується лише після проходження сигналу через кілька рівнів логіки. Затримка поширення <span class="formula">\(t_{pd}\)</span> для мікросхем серії HC становить близько 15–20 нс на каскад. Якщо зчитати результат порівняння до завершення цього часу встановлення, схема зафіксує невірні проміжні перехідні стани.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
