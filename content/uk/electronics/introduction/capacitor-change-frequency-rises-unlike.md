---
id: emb-elintro-0140
title: "Як змінюється `X_C` конденсатора зі зростанням частоти – на відміну від `X_L`?"
description: "Як змінюється XC конденсатора зі зростанням частоти – на відміну від XL?"
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
    applicability: "Походження питання: лекція 14, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-capacitor-reactance-precise
    title: "All About Circuits: AC Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/ac-capacitor-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Формула ідеального ємнісного реактансу та його обернена залежність від частоти; твердження про фільтри потребують конкретної схеми."
---

## Short answer

Для ідеального конденсатора `X_C = 1/(2π*f*C)`, тому реактанс спадає зі зростанням частоти. У порівнянні, `X_L = 2π*f*L` зростає; твердження про пропускання сигналів залежить від усієї схеми, а не лише компонента.[^aac-capacitor-reactance-precise]

## Detailed explanation

Ємнісний реактанс ідеального конденсатора для sinusoidal AC визначається формулою `X_C = 1/(2π*f*C)`, де `f` – частота в герцах, а `C` – ємність у фарадах. Оскільки частота стоїть у знаменнику, за незмінної ємності реактанс обернено пропорційний частоті: подвоєння частоти вдвічі зменшує `X_C`.[^aac-capacitor-reactance-precise]

Причина пов’язана зі співвідношенням між струмом і зміною напруги на конденсаторі. За вищої частоти напруга змінюється швидше, тому конденсатор може проводити більший змінний струм за тієї самої амплітуди напруги. Для ідеального DC, коли частота дорівнює нулю після перехідного процесу, конденсатор поводиться як розрив кола; реальний компонент має витік та паразитні ефекти.[^aac-capacitor-reactance-precise]

Для порівняння індуктивний реактанс `X_L = 2π*f*L` зростає з частотою, тож ідеальні C та L мають протилежну частотну залежність. Наприклад, якщо частоту синусоїди подвоїти, `X_C` зменшиться вдвічі, а `X_L` збільшиться вдвічі за незмінних `C` та `L`. Реактанси обох компонентів вимірюються в омах, але вони не є резистивними втратами.[^aac-capacitor-reactance-precise]

Не можна лише з формули зробити універсальний висновок «конденсатор пропускає ВЧ». Фактична передача сигналу залежить від топології, джерела й навантаження: у послідовному RC-колі та паралельному з’єднанні функція компонента різна. На дуже високих частотах паразитна індуктивність і опір також порушують ідеальну модель.

**Типова помилка:** плутати низький `X_C` компонента із гарантованим проходженням сигналу через будь-яку схему.

## Sources

<!-- generated from frontmatter -->
