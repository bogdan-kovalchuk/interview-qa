---
id: emb-elee-0036
title: "Яка частка енергії джерела розсіюється на резисторі при заряджанні конденсатора через R від сталої напруги?"
description: "Яка частка енергії джерела розсіюється на резисторі при заряджанні конденсатора через R від сталої напруги?"
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
    applicability: "Походження питання: лекція 37, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: openstax-rc-circuits
    title: "OpenStax University Physics Volume 2: 10.5 RC Circuits"
    url: https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits
    accessed: 2026-10-04
    kind: book
    version: "University Physics Volume 2"
    applicability: "Енергія накопичена в конденсаторі та заряджання через резистор від сталої ідеальної напруги; висновок про частку втрат спирається на інтегрування потужності для цієї схеми."
  - source_id: openstax-capacitor-energy
    title: "OpenStax University Physics Volume 2: 8.3 Energy Stored in a Capacitor"
    url: https://openstax.org/books/university-physics-volume-2/pages/8-3-energy-stored-in-a-capacitor
    accessed: 2026-10-04
    kind: book
    version: "University Physics Volume 2"
    applicability: "Формула енергії, запасеної в конденсаторі; сама по собі не визначає розподіл енергії джерела."
---

## Short answer

Для початково розрядженого конденсатора, який заряджають від ідеального джерела сталої напруги `V_0` через резистор, половина енергії, відданої джерелом, накопичується в конденсаторі, а половина розсіюється в резисторі. Кінцева енергія конденсатора дорівнює `E_C = C*V_0^2/2`; результат не залежить від `R`, якщо заряджання завершене.[^openstax-rc-circuits]

## Detailed explanation

Для такого результату важливо точно визначити, з чим порівнюємо енергії: джерело віддає загалом `E_source = C*V_0^2`, а не `C*V_0^2/2`. Половина цієї енергії залишається в електричному полі конденсатора, а друга половина перетворюється на тепло в резисторі під час перехідного процесу.[^openstax-rc-circuits]

Нехай спочатку конденсатор не заряджений, ідеальне джерело підтримує сталу напругу `V_0`, а між ним і конденсатором послідовно стоїть резистор `R`. Після повного заряджання заряд дорівнює `Q = C*V_0`. Робота джерела дорівнює його сталій напрузі, помноженій на повний перенесений заряд: `E_source = V_0*Q = C*V_0^2`.[^openstax-rc-circuits]

Енергія, що лишилася в конденсаторі, обчислюється як `E_C = C*V_0^2/2`.[^openstax-capacitor-energy] Різниця між переданою джерелом енергією та кінцевою енергією конденсатора і є втратами в резисторі: `E_R = E_source - E_C = C*V_0^2/2`. Отже, частка розсіяної енергії від енергії джерела становить `E_R/E_source = 1/2`.[^openstax-rc-circuits]

**Приклад розрахунку:** для `C = 100 µF` і `V_0 = 10 V` джерело віддає `E_source = 0.0001*10^2 = 0.01 J`; конденсатор зберігає `0.005 J`, а резистор розсіює `0.005 J`. Значення `R` визначає тривалість заряджання `τ = R*C`, але не цей енергетичний поділ за умови, що інтегруємо весь процес до усталеного стану.[^openstax-rc-circuits]

У реальному колі частина енергії може втрачатися ще в джерелі, проводах та інших елементах, а опір джерела також впливає на те, де саме виділяється тепло. Тому вислів «половина розсіюється на резисторі» описує саме ідеальне коло з одним послідовним резистором і сталим джерелом, а не будь-яке практичне заряджання.[^openstax-rc-circuits]

**Типова помилка:** називати `C*V_0^2/2` енергією, яку віддало джерело. Це кінцева енергія конденсатора; джерело передає вдвічі більше в цій ідеалізованій схемі.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
