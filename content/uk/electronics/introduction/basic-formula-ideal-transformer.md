---
id: emb-elintro-0149
title: "Яка основна формула ідеального трансформатора?"
description: "Яка основна формула ідеального трансформатора?"
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 15, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-transformer-ratio
    title: "All About Circuits: Step-up and Step-down Transformers"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-9/step-up-and-step-down-transformers/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Співвідношення витків і напруги та обернене співвідношення струмів у трансформаторній моделі; практичні втрати потребують окремого врахування."
---

## Short answer

Для ідеального трансформатора `V₁/V₂ = N₁/N₂`, де `N₁` і `N₂` – кількість витків первинної та вторинної обмоток. Струми мають обернене співвідношення: `I₁/I₂ = N₂/N₁`; тому в ідеальній моделі `V₁*I₁ = V₂*I₂`.[^aac-transformer-ratio]

## Detailed explanation

Ідеальний трансформатор передає енергію між двома обмотками через спільний змінний магнітний потік в осерді. Для синусоїдального режиму напруга кожної обмотки пропорційна кількості її витків, тому відношення напруг дорівнює відношенню витків: `V₁/V₂ = N₁/N₂`. Тут індекси 1 і 2 позначають первинну й вторинну сторони; важливо порівнювати напруги одного типу, зазвичай RMS для синусоїди.[^aac-transformer-ratio]

За ідеального зчеплення та відсутності втрат потужність на вході дорівнює потужності на виході. Отже, підвищення напруги супроводжується зменшенням струму в оберненій пропорції, а зниження напруги – збільшенням доступного струму. Це не створює додаткової потужності: навантаження визначає фактичний вторинний струм, а первинна сторона споживає відповідну потужність.[^aac-transformer-ratio]

**Приклад розрахунку:**

```text
N₁ = 100, N₂ = 500
V₁ = 12 V
V₂ = V₁ * N₂/N₁ = 12 * 5 = 60 V
```

Це оцінка для ідеальної моделі за умов, що трансформатор працює зі змінним потоком і не насичує осердя. Реальний пристрій має опір обмоток, витоки потоку та втрати в осерді, а напруга під навантаженням відрізняється від ідеального розрахунку. Звичайний трансформатор не передає сталу DC-напругу: після короткого перехідного процесу сталий потік не індукує вторинну напругу, тоді як прикладена DC може спричинити надмірний струм у первинній обмотці.[^aac-transformer-ratio]

**Типова помилка:** плутати напрямок відношення. Якщо вторинна обмотка має більше витків, її напруга в ідеальному режимі більша, але можливий вихідний струм менший за того самого рівня переданої потужності. Для вибору реального трансформатора додатково перевіряють номінальну частоту, напруги, потужність і допустиме навантаження.[^aac-transformer-ratio]

## Sources

<!-- generated from frontmatter -->
