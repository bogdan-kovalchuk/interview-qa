---
id: emb-elinteg-0020
title: "Навіщо в аналоговому мультиплексорі 74HC4051 передбачено окремий вивід живлення VEE?"
description: "Навіщо в аналоговому мультиплексорі 74HC4051 передбачено окремий вивід живлення VEE?"
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 94 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Вивід VEE є негативною шиною живлення внутрішніх аналогових ключів і дозволяє комутувати двополярні аналогові сигнали (наприклад, аудіо). Напруга аналогового сигналу може змінюватися в діапазоні від VEE до VCC, тоді як цифрове керування здійснюється відносно GND. Якщо комутуються лише однополярні позитивні напруги, вивід VEE з'єднують із землею GND.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
