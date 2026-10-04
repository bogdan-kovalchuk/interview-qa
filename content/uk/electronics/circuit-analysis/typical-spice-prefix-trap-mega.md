---
id: emb-elcirc-0039
title: "Яка типова пастка з префіксом mega у ngspice?"
description: "Яка типова пастка з префіксом mega у ngspice?"
track: electronics
section: circuit-analysis
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
    applicability: "Походження питання: лекція 31, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: ngspice-number-suffixes
    title: "ngspice User's Manual: Some naming conventions"
    url: https://nmg.gitlab.io/ngspice-manual/circuitdescription/generalstructureandconventions/somenamingconventions.html
    accessed: 2026-10-04
    kind: official
    version: "current manual"
    applicability: "Визначає суфікси чисел у ngspice: m означає 10^-3, Meg – 10^6; інші SPICE-сумісні програми можуть мати окремі правила."
---

## Short answer

У ngspice суфікс `m` означає мілі (10^-3), а `Meg` – мега (10^6), незалежно від регістру літер.[^ngspice-number-suffixes] Тому `1M` означає 1 mΩ у значенні числового суфікса, а для 1 MΩ слід записати `1Meg`.[^ngspice-number-suffixes] Правила можуть залежати від конкретного SPICE-сумісного симулятора, тому їх перевіряють у його manual.[^ngspice-number-suffixes]

## Detailed explanation

У ngspice літера `m` у суфіксі числового значення означає milli, тобто множник 10^-3; для mega застосовують `Meg`, множник 10^6.[^ngspice-number-suffixes]

Це відрізняється від звичного запису SI, де велика літера M позначає mega. ngspice читає суфікси без розрізнення регістру, тому `M` і `m` не можуть бути двома різними одиницями: обидва означають milli. Відповідно, у рядку резистора `R1 in out 1M` значення буде одним міліом, а не одним мегаом. Для резистора 1 MΩ напишіть `R1 in out 1Meg`.[^ngspice-number-suffixes]

Ця плутанина змінює значення в мільярд разів: співвідношення 10^6 / 10^-3 = 10^9. У простому дільнику це може перетворити очікуваний великий опір на майже коротке замикання та змінити і струми, і вихідну напругу. Варто пам’ятати й інші суфікси: `k` означає 10^3, `u` – 10^-6, а `n` – 10^-9; текстові одиниці після суфікса не обов’язково надають значенню потрібну величину.[^ngspice-number-suffixes]

Не слід автоматично узагальнювати це правило на всі симулятори. LTspice, ngspice та інші програми можуть приймати близький, але не тотожний синтаксис або додаткові суфікси. Для відтворюваного netlist вкажіть, який simulator використовуєте, та звіряйте notation з його документацією; для переносимого прикладу можна записати степінь через експоненційний формат, якщо його підтримка підтверджена.[^ngspice-number-suffixes]

**Типова помилка:** бачити в `1M` стандартне позначення мега й не перевіряти правила парсера. У ngspice для мега використовуйте `Meg`, а потім перевірте вимірювану чи розраховану величину на очікуваний порядок.[^ngspice-number-suffixes]

## Sources

<!-- generated from frontmatter -->
