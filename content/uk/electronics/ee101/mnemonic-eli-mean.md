---
id: emb-elee-0049
title: "Що означає мнемоніка ELI?"
description: "Що означає мнемоніка ELI?"
track: electronics
section: ee101
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
    applicability: "Походження питання: лекція 40, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: phase-basics
    title: "Phase Relationships in Inductive and Capacitive Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/phase-relationships/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Фазові співвідношення ідеальних L та C; обґрунтовує значення ELI/ICE."
---

## Short answer

ELI означає: в індукторі (`L`) напруга (`E`, electromotive force) випереджає струм (`I`) на 90° у синусоїдальному усталеному режимі. Парна мнемоніка ICE нагадує, що в конденсаторі струм випереджає напругу на 90°.[^phase-basics]

## Detailed explanation

У мнемоніці ELI літери допомагають згадати фазовий порядок в індукторі: `E` (напруга, або electromotive force) випереджає `I` (струм) у `L` на 90°. Це узгоджується з рівнянням `v = L*di/dt`: напруга пропорційна похідній струму, а похідна синусоїди випереджає вихідну синусоїду на чверть періоду.[^phase-basics]

Для конденсатора застосовують парну мнемоніку ICE: `I` випереджає `E` у `C`. Рівняння `i = C*dv/dt` пояснює цю фазову залежність. «Випереджає» означає, що відповідний максимум синусоїди настає раніше; кут 90° відповідає четверті періоду, а часова відстань між максимумами залежить від частоти сигналу.[^phase-basics]

Наприклад, за частоти `50 Hz` період становить `20 ms`, а чверть періоду – `5 ms`. В ідеальному індукторі напруга досягає максимуму на `5 ms` раніше за струм. У реального індуктора є опір обмотки й паразитні ефекти, тому кут між повною напругою та струмом може відрізнятися від 90°.[^phase-basics]

**Типова помилка:** прочитати ELI так, ніби струм випереджає напругу. Розгорніть літери як мнемонічний порядок: `E` перед `I` в `L`; для конденсатора `I` перед `E` в `C`. Правило стосується синусоїдального усталеного режиму, а не перехідного процесу чи постійної напруги, для яких фазове випередження не є потрібним описом.

## Sources

<!-- generated from frontmatter -->
