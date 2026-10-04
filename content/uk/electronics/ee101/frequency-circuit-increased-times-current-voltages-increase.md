---
id: emb-elee-0080
title: "Якщо частоту в RL-колі збільшити в 10 разів, чи зростуть струм і напруги так само в 10 разів?"
description: "Якщо частоту в RL-колі збільшити в 10 разів, чи зростуть струм і напруги так само в 10 разів?"
track: electronics
section: ee101
level: junior
type: pitfall
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
    applicability: "Походження питання: лекція 45, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-series-rl
    title: "All About Circuits: Series Resistor-Inductor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/series-resistor-inductor-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтримує комплексний імпеданс послідовного RL-кола, фазорні напруги та їхній векторний, а не скалярний розрахунок."
---

## Short answer

Ні. За сталої індуктивності `X_L = 2π*f*L`, тому десятикратна частота дає десятикратну індуктивну реактивність, але струм і напруги залежать від повного комплексного імпедансу кола. Напруги на резисторі й котушці є фазорами, тож їхні модулі не додають як звичайні числа.[^aac-series-rl]

## Detailed explanation

У послідовному RL-колі частота змінює індуктивну реактивність, але не масштабує автоматично всі струми й напруги в однакову кількість разів. Для ідеальної котушки `X_L = 2π*f*L`: якщо `L` стала, збільшення `f` у десять разів справді збільшує `X_L` у десять разів. Проте імпеданс усього кола дорівнює `Z = R + j*X_L`, а струм визначає співвідношення `I = V_in/Z`; отже його модуль залежить від R та початкового співвідношення між R і `X_L`.[^aac-series-rl]

Напруга на резисторі дорівнює `V_R = I*R`, а на котушці – `V_L = I*j*X_L`. Коли змінюється частота, змінюються і струм, і фазовий кут імпедансу. Тому на одному виході напруга може зменшитися, на іншому – зрости або наблизитися до межі, але не зобов’язана змінюватися в десять разів. У точному розрахунку ці напруги додаються як комплексні величини за законом Кірхгофа, а не як їхні додатні модулі.[^aac-series-rl]

Приклад: нехай вхідна синусоїда має сталу амплітуду, а опір R дорівнює реактивності котушки на початковій частоті. Тоді модуль імпедансу дорівнює `√2*R`; після збільшення частоти в десять разів він дорівнює `√101*R`. Отже, модуль струму зменшиться у `√(101/2)`, приблизно у 7.1 раза, а не зросте вдесятеро. Це ілюстрація для ідеальних компонентів і незмінного джерела, а не універсальне число для будь-якого RL-кола.[^aac-series-rl]

**Типова помилка:** помітити десятикратне зростання `X_L` і зробити висновок, що так само зростуть струм чи кожен спад напруги. Перед відповіддю слід перевірити схему, місце виходу, амплітуду джерела та початкові значення R і L, а тоді перерахувати комплексний дільник для обох частот. Реальна котушка має втрати та паразитні параметри, тому модель `j*ω*L` справджується лише в межах її робочого діапазону.[^aac-series-rl]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
