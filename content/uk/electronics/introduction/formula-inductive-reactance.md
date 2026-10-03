---
id: emb-elintro-0139
title: "Формула індуктивного реактансу `X_L`?"
description: "Формула індуктивного реактансу XL?"
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
  - source_id: aac-inductor-reactance-precise
    title: "All About Circuits: AC Inductor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/ac-inductor-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Формула ідеального індуктивного реактансу та його пропорційність частоті; реальні втрати й parasitic effects не описані формулою."
---

## Short answer

Для ідеальної котушки в sinusoidal AC індуктивний реактанс `X_L = 2π*f*L`, вимірюється в омах і зростає з частотою. Це реактанс, а не звичайний опір; реальна котушка має втрати та паразитні параметри.[^aac-inductor-reactance-precise]

## Detailed explanation

Індуктивний реактанс ідеальної котушки в усталеному sinusoidal AC дорівнює `X_L = 2π*f*L`, де `f` – частота в герцах, а `L` – індуктивність у генрі. Результат вимірюється в омах. Множник `2π*f` є кутовою частотою, тому за незмінної індуктивності реактанс прямо пропорційний частоті.[^aac-inductor-reactance-precise]

Фізичний зв’язок походить від поведінки індуктора: він створює напругу пропорційну швидкості зміни струму. Синусоїда вищої частоти змінюється швидше, тому для неї потрібна більша напруга на тій самій індуктивності й амплітуді струму. У чисто ідеальному випадку при постійному струмі `f = 0`, отже індуктивний реактанс дорівнює нулю; це не враховує опір дроту реальної обмотки.[^aac-inductor-reactance-precise]

Приклад: для `L = 10 mH = 0.01 H` на частоті `1 kHz` реактанс приблизно `2π*1000*0.01 ≈ 62.8 Ω`. Це не означає, що котушка є резистором на 62.8 Ω: реактанс пов’язаний із фазовим зсувом і обміном енергією з полем. У змішаному колі струм визначають повним імпедансом, що враховує також резистивні компоненти.[^aac-inductor-reactance-precise]

Формула описує ідеальну модель. У реальної котушки є опір обмотки, паразитна ємність та втрати в осерді; біля і вище власної резонансної частоти поведінка може відрізнятися від простого зростання `X_L`.

**Типова помилка:** підставляти частоту в кілогерцах як число без перерахунку в герци або називати `X_L` омічним опором котушки.

## Sources

<!-- generated from frontmatter -->
