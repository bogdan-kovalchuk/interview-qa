---
id: emb-elintro-0095
title: "Що таке коефіцієнт потужності cos(θ) і чому він важливий для енергетики?"
description: "Що таке коефіцієнт потужності cos(θ) і чому він важливий для енергетики?"
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
    applicability: "Походження питання: лекція 10, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-power-factor
    title: "All About Circuits: Calculating Power Factor"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/calculating-power-factor/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Визначає коефіцієнт потужності синусоїдального кола та пояснює вплив реактивної потужності на струм лінії й корекцію."
  - source_id: aac-sinusoidal-real-power
    title: "All About Circuits: Sinusoidal Steady-State Power Calculations"
    url: https://www.allaboutcircuits.com/technical-articles/sinusoidal-steady-state-power-calculations/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтримує співвідношення між активною потужністю, RMS-значеннями та фазовою різницею для синусоїдальних сигналів."
---

## Short answer

Для синусоїдального кола коефіцієнт потужності дорівнює `PF = P/S = cos(phi)`, де `S = V_rms*I_rms`, а `phi` – різниця фаз напруги й струму. Нижчий `PF` означає більший струм для передавання тієї самої активної потужності за тієї самої напруги; для індуктивного навантаження його часто коригують конденсаторами поблизу навантаження.[^aac-power-factor]

## Detailed explanation

Коефіцієнт потужності `PF` показує, наскільки ефективно змінний струм переносить активну потужність до навантаження. Для синусоїдальних сигналів `PF = P/S = cos(phi)`, де `P` – середня активна потужність у ватах, `S = V_rms*I_rms` – повна потужність у вольт-амперах, а `phi` – кут між фазами напруги й струму. Отже, `cos(phi)` є коефіцієнтом потужності за синусоїдальних умов, а не окремою потужністю.[^aac-power-factor]

Коли коефіцієнт потужності нижчий за одиницю, для тієї самої активної потужності й напруги потрібен більший струм лінії: `I = P/(V*PF)` для однофазного синусоїдального кола. Більший струм збільшує втрати `I^2*R` у проводах і навантажує джерело та обладнання. Ідеальне резистивне навантаження має `PF = 1`; ідеально реактивне навантаження має нульову середню активну потужність, хоча струм у ньому може бути значним.[^aac-power-factor] [^aac-sinusoidal-real-power]

Для індуктивного навантаження, наприклад двигуна, паралельний конденсатор може компенсувати частину індуктивної реактивної потужності й зменшити струм, який надходить із мережі. Його підбирають для конкретної установки: надмірна ємність може перекомпенсувати навантаження. Конденсатор не усуває всю реактивну циркуляцію всередині гілки навантаження й не замінює оцінку гармонік або змінного режиму споживання.[^aac-power-factor]

Приклад: для однофазного навантаження `P = 10 kW` при `V = 230 V` та `PF = 0.5` струм становить приблизно `87 A`; за `PF = 1` для тієї самої активної потужності він був би приблизно `43 A`. Це спрощене порівняння припускає синусоїдальний режим і незмінну напругу.[^aac-power-factor]

**Типові помилки:**
- Називати коефіцієнт потужності часткою «корисної» енергії без визначення повної потужності та режиму сигналів.
- Вважати, що `cos(phi)` повністю описує коефіцієнт потужності за спотвореного струму: для несинусоїдальних сигналів гармоніки також впливають на відношення `P/S`.[^aac-power-factor]

## Sources

<!-- generated from frontmatter -->
