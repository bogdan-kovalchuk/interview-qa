---
id: emb-elee-0118
title: "Як побудований RL-фільтр високих частот?"
description: "Як побудований RL-фільтр високих частот?"
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
    applicability: "Походження питання: лекція 53, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-high-pass-filters
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Топологія RL-ФВЧ із послідовним резистором, індуктивністю паралельно до навантаження, гранична частотна поведінка та ефект втрат у реальній котушці."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

Резистор увімкнено послідовно з джерелом, котушку – від вихідного вузла до спільного проводу, а вихід знімають із вузла, паралельно котушці. На DC імпеданс ідеальної котушки дорівнює нулю, а зі зростанням частоти збільшується, тож вихід наближається до входу.[^aac-high-pass-filters]

## Detailed explanation

RL-ФВЧ можна побудувати з резистора, увімкненого послідовно з джерелом, і котушки, з’єднаної від вихідного вузла до спільного проводу; вихід знімають із вузла, тобто паралельно котушці. На низькій частоті імпеданс L малий, тому котушка відводить сигнал до спільного проводу. На високій частоті її імпеданс більший, тож вихід наближається до вхідної напруги.[^aac-high-pass-filters]

Якщо навантаженням є сам вхід наступного каскаду і його впливом можна знехтувати, ідеальна передавальна функція має вигляд `H(jω) = jωL/(R + jωL)`. Модуль зростає від нуля на DC до одиниці на високих частотах; на частоті `f_c = R/(2π*L)` він дорівнює приблизно 0.707 від високочастотного рівня. Реальне навантаження паралельно котушці змінює еквівалентний опір і характеристику, тож формула з одним R не є універсальною для будь-якого підключення.[^aac-high-pass-filters]

Приклад: якщо `R = 1 kΩ` і `L = 2.2 mH`, то `f_c ≈ 72.3 kHz`. Нижче зрізу амплітуда зростає приблизно пропорційно частоті, а значно вище зрізу вихід наближається до входу. Не плутайте цю схему з RL-ФНЧ: там котушка стоїть послідовно в сигнальному шляху, а вихід беруть на резисторі. У реальній котушці опір обмотки й паразитні параметри змінюють низькочастотне передавання та верхню межу корисного діапазону.[^aac-high-pass-filters]

## Sources

<!-- generated from frontmatter -->
