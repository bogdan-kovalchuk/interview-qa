---
id: emb-elee-0048
title: "Які інструменти використовують для перевірки розрахунків RC/RL-кіл?"
description: "Які інструменти використовують для перевірки розрахунків RC/RL-кіл?"
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
    applicability: "Походження питання: лекція 39, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: simulink-simulation
    title: "Simulation - MATLAB & Simulink"
    url: https://www.mathworks.com/help/simulink/simulation.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Моделювання безперервних, дискретних і змішаних систем у Simulink."
  - source_id: ltspice-ac
    title: ".AC -- Perform an AC analysis"
    url: https://ltwiki.org/LTspiceHelpXVII/LTspiceHelp/html/AC_analysis.htm
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "LTspice малосигнальний AC аналіз біля DC робочої точки."
---

## Short answer

Для перевірки розрахунків можна побудувати аналітичну криву в MATLAB/Simulink і порівняти її зі SPICE-моделлю: `.tran` показує перехідний процес, а `.ac` – малосигнальну частотну характеристику. Симуляція перевіряє лише задану модель, тому схема, номінали й початкові умови мають бути правильними.[^simulink-simulation]

## Detailed explanation

Розрахунок RC/RL-кола зручно перевіряти аналітично, симуляцією та, коли доступно, вимірюванням. MATLAB може побудувати очікувану криву за рівнянням, а Simulink моделює динамічну систему чисельними методами. SPICE дає змогу задати конкретну схему з джерелами, компонентами та навантаженнями. Незалежність методів корисна: помилка в алгебрі може бути помітна у симуляції, а помилка у схемному з’єднанні – під час звірки з формулою.[^ltspice-ac]

Transient аналіз показує зміну сигналу з часом: наприклад, чи наближається напруга конденсатора до правильного усталеного значення та чи відповідає швидкість зміни сталому часу. В LTspice для нього задають `.tran`. Команда `.ac` виконує малосигнальний аналіз у частотній області біля DC робочої точки, тому підходить для частотної характеристики лінійного режиму, але не замінює аналіз великих перехідних сигналів.[^ltspice-ac]

Перед порівнянням узгодьте схему, одиниці, полярність, амплітуду джерела, навантаження та початкову напругу конденсатора або струм індуктора. За різних початкових умов результати цілком можуть розійтися без помилки в будь-якому інструменті. Так само ідеальний симулятор не врахує паразитні параметри компонента, якщо модель їх не містить.[^ltspice-ac]

Приклад: за `R = 1 kΩ` і `C = 100 nF` маємо `τ = 100 µs`. У transient аналізі заряджання після `100 µs` конденсатор проходить близько 63.2% шляху від початкової до кінцевої напруги. Для ненавантаженого RC low-pass той самий ланцюг має частоту зрізу `f_c = 1/(2*π*τ) ≈ 1.59 kHz`; її можна перевірити `.ac` графіком.[^ltspice-ac]

**Типова помилка:** вважати збіг із симулятором доказом. Перевірте введену схему та моделі компонентів, а щонайменше одну точку порівняйте з ручним розрахунком або вимірюванням.

## Sources

<!-- generated from frontmatter -->
