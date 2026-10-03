---
id: emb-elintro-0182
title: "Орієнтовна формула ripple для конденсатора після випрямляча?"
description: "Орієнтовна формула ripple для конденсатора після випрямляча?"
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
    applicability: "Походження питання: лекція 17, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: power-com-rectifier-capacitor
    title: "AN-92: Input Capacitor Derivation"
    url: https://www.power.com/sites/default/files/documents/an-92_mine-cap_design_guide.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Описує повнохвильовий міст із накопичувальним конденсатором і виведення його поведінки; проста оцінка пульсацій залежить від навантаження та ємності."
---

## Short answer

Для грубої оцінки: `ΔV ≈ I_load/(f_ripple*C)`. У bridge rectifier `f_ripple` удвічі більша за частоту мережі: `100 Hz` для `50 Hz` або `120 Hz` для `60 Hz`.[^power-com-rectifier-capacitor]

## Detailed explanation

Формула `ΔV ≈ I_load/(f_ripple*C)` оцінює peak-to-peak пульсації: між вершинами випрямленої напруги конденсатор віддає заряд навантаженню, а наступна вершина знову його підзаряджає. За приблизно сталого струму `I = C*ΔV/Δt`, а проміжок між вершинами дорівнює `1/f_ripple`.[^aac-semiconductors]

У повнохвильовому мосту кожна півхвиля змінного сигналу дає імпульс тієї самої полярності, тому частота пульсацій удвічі більша за частоту мережі: `100 Hz` для `50 Hz` і `120 Hz` для `60 Hz`. У напівхвильовому випрямлячі імпульси надходять лише раз за період, тож за однакових ємності й навантаження оцінка пульсацій приблизно вдвічі більша.[^aac-semiconductors]

Приклад розрахунку: навантаження споживає `0.1 A`, конденсатор має `1000 µF`, мережа – `50 Hz` із мостом. Тоді `ΔV ≈ 0.1/(100*0.001) = 1 V`. Це спрощення: фактична форма залежить від опору трансформатора й діодів, ESR конденсатора, характеру навантаження та кута провідності діодів.[^aac-semiconductors]

**Типова помилка:** підставляти `50 Hz` замість `100 Hz` для моста або вважати оцінку гарантованою межею. Для проєктування перевіряють мінімальну напругу на навантаженні й допустимий ripple current конденсатора, а потім вимірюють пульсації в реальній схемі.

## Sources

<!-- generated from frontmatter -->
