---
id: emb-elee-0184
title: "Чому великий електролітичний конденсатор не завжди усуває швидкі завади?"
description: "Чому великий електролітичний конденсатор не завжди усуває швидкі завади?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Походження питання: лекція 66, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; курс не є доказом цих тверджень."
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
  - source_id: ti-switching-regulator-fundamentals
    title: "Texas Instruments: Switching regulator fundamentals"
    url: https://www.ti.com/lit/an/snva559c/snva559c.pdf
    accessed: 2026-10-13
    kind: official
    version: "Rev. C"
    applicability: "Записка про імпульсні регулятори: ESL обмежує алюмінієвий електроліт на високих частотах, ESR, ESL і C утворюють резонансний контур; електроліт шунтують плівковим і керамічним конденсаторами; виводи живлення IC шунтують до землі з малою індуктивністю, локальні bypass-конденсатори – керамічні або плівкові. Конкретні значення беруть з datasheet."
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
    accessed: 2026-10-13
    kind: book
    version: "1.1.2, 22 April 2021"
    applicability: "Рівняння ідеальних елементів: v = L*di/dt для котушки (зміна струму дає напругу). Опору та паразитних параметрів ідеальних елементів документ не моделює."
---

## Short answer

На високих частотах дію електролітичного конденсатора обмежують його ESR, паразитна індуктивність ESL і довгі з’єднання.[^ti-switching-regulator-fundamentals] Тому потрібні локальні керамічні bypass-конденсатори на виводах живлення мікросхеми.[^ti-switching-regulator-fundamentals]

## Detailed explanation

Велика електролітична ємність добре тримає низькочастотні пульсації, але на високих частотах вона поводиться не як ідеальна ємність. Паразитний послідовний опір ESR, паразитна індуктивність ESL і ємність C утворюють резонансний контур, а ESL обмежує ефективність конденсатора на високих частотах.[^ti-switching-regulator-fundamentals] Тому електроліт сам по собі не гасить швидкі завади, навіть коли його ємність велика.

Для великих імпульсних струмів TI рекомендує поєднувати алюмінієвий електроліт із плівковим і керамічним конденсаторами.[^ti-switching-regulator-fundamentals] Ілюстративний розрахунок (значення не належать конкретному конденсатору): на частоті 100 МГц індуктивність 10 нГн дає опір `2*pi*f*L ≈ 6,3 Ом`, а ємнісний опір 100 мкФ на тій самій частоті становить близько `0,000016 Ом`. На цій частоті електролітичний конденсатор фактично є індуктивністю, і його ємність майже не впливає на шунтування.

Тому високі частоти шунтують малоіндуктивні керамічні або плівкові конденсатори, поставлені поруч із мікросхемою. Усі виводи живлення мікросхеми треба шунтувати до чистої землі з малою індуктивністю.[^ti-switching-regulator-fundamentals] Довга доріжка до великого конденсатора додає індуктивність, і швидкий струм на ній створює падіння напруги `L*di/dt`, яке далекий електроліт не може компенсувати.[^fiore-ac-circuit-analysis]

**Типові помилки:**

- Вважати, що велика електролітична ємність на вході плати замінює bypass біля мікросхеми.
- Ставити керамічний конденсатор далеко від мікросхеми через довгу доріжку до землі: індуктивність доріжки значно зменшує його дію.
- Вважати електроліт зайвим: для великих імпульсних струмів його рекомендують разом із плівковим і керамічним конденсаторами, він лише не покриває високі частоти сам.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
