---
id: emb-elee-0041
title: "Як наростає струм у RL-колі після подачі напруги і яка його постійна часу?"
description: "Як наростає струм у RL-колі після подачі напруги і яка його постійна часу?"
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
    applicability: "Походження питання: лекція 38, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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

Для ідеального послідовного RL-кола зі сталим джерелом `V_0` і нульовим початковим струмом `I(t) = (V_0/R)*(1 - e^(-t/τ))`, де `τ = L/R`. Через `5τ` струм становить приблизно 99.3% від `V_0/R`; ця оцінка передбачає сталі `R` та `L`.[^aac-alternating-current]

## Detailed explanation

У послідовному RL-колі після прикладання сталої напруги струм не стрибає миттєво до значення, яке задає резистор. Зміна струму створює напругу на індукторі, пропорційну швидкості зміни струму, тому на початку більша частина напруги джерела припадає на індуктор.[^aac-alternating-current]

Для ідеального індуктора та резистора закон Кірхгофа дає `V_0 = I*R + L*dI/dt`. Після вмикання джерела з початковою умовою `I(0) = 0` розв’язок прямує до усталеного значення `I_final = V_0/R`. Стала часу `τ = L/R` визначає швидкість: через одну `τ` струм проходить приблизно 63.2% різниці між початковим та кінцевим значеннями, а через п’ять сталих часу – приблизно 99.3%.[^aac-alternating-current]

Приклад: нехай `L = 10 mH`, `R = 100 Ω`, `V_0 = 5 V`. Тоді `τ = 0.01/100 = 0.0001 s = 0.1 ms`, а кінцевий струм дорівнює `5/100 = 0.05 A`. За `0.5 ms`, тобто `5τ`, струм буде приблизно `0.05*(1 - e^(-5)) ≈ 0.0497 A`. Це розрахунок для сталої напруги й лінійної моделі; опір джерела та обмотки слід додати до `R`, якщо вони істотні.[^aac-alternating-current]

**Типові помилки:**

- Плутати сталу часу RL-кола `L/R` зі сталою часу RC-кола `R*C`.
- Вважати, що через `5τ` струм математично точно дорівнює кінцевому значенню; експонента лише наближається до нього.
- Забувати початковий струм. Для іншого `I(0)` змінюється амплітуда експоненційної складової.[^aac-alternating-current]

## Sources

<!-- generated from frontmatter -->
