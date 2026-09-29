---
id: emb-elinteg-0012
title: "Чому не можна обмежувати струм семисегментного індикатора одним загальним резистором в аноді?"
description: "Чому не можна обмежувати струм семисегментного індикатора одним загальним резистором в аноді?"
track: electronics
section: digital-integration
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
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 92 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, комбінаційні та послідовні інтегральні схеми, регістри зсуву й АЛП."
---

## Short answer

Якщо встановити один резистор у спільному аноді, сумарний струм розподілятиметься між усіма увімкненими сегментами. При відображенні цифри 1 струм ділиться між двома сегментами, а при цифрі 8 – між сімома, через що яскравість цифри 8 буде в рази меншою. Правильна схемотехніка вимагає встановлення окремого струмообмежувального резистора для кожного сегмента.[^udemy-electronics-course]

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
