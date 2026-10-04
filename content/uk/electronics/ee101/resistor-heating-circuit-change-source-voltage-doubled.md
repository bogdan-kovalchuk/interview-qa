---
id: emb-elee-0089
title: "Як зміниться нагрівання резистора в RC-колі, якщо подвоїти напругу джерела при тих самих R, C і частоті?"
description: "Як зміниться нагрівання резистора в RC-колі, якщо подвоїти напругу джерела при тих самих R, C і частоті?"
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
    applicability: "Походження питання: лекція 47, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
---

## Short answer

За незмінних R, C і частоти подвоєння синусоїдальної напруги подвоює струм та збільшує середню потужність у R учетверо: `P_R = I_RMS^2*R`.[^aac-alternating-current] Це припускає лінійні компоненти, що не перегріваються й не змінюють параметрів.[^aac-alternating-current]

## Detailed explanation

У лінійному RC-колі з незмінними R, C і частотою повний імпеданс сталий, тому струм пропорційний напрузі джерела. Подвоєння напруги подвоює струм, а резистивна потужність залежить від квадрата струму: `P_R = I_RMS^2*R`.[^aac-alternating-current]

Цей висновок стосується середньої потужності за період синусоїдального сигналу. У формулі використовують RMS-струм; для синусоїди `I_RMS = I_peak/sqrt(2)`. Якщо подвоїти peak voltage, RMS напруга також подвоїться, отже той самий коефіцієнт чотири залишається для середнього нагрівання.[^aac-alternating-current]

Розрахунок передбачає лінійний режим: опір не змінюється від температури, конденсатор не пробитий, джерело утримує задану форму сигналу, а частота та навантаження сталі. У реальному колі значне нагрівання може змінити опір резистора, а обмеження генератора або насичення іншого елемента порушать просту пропорційність. Тоді потрібно виміряти фактичний RMS-струм і обчислити потужність за ним.[^aac-alternating-current]

**Типові помилки:**
- Подвоювати потужність лише вдвічі, бо напруга подвоїлася.
- Підставляти peak current у RMS-формулу без коефіцієнта для синусоїди.

Наприклад, якщо спочатку `I_RMS = 10 mA` і `R = 100 Ω`, то потужність становить `10 mW`. Після подвоєння напруги й струму до `20 mA RMS` потужність дорівнює `40 mW`, тобто зросла вчетверо.[^aac-alternating-current]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
