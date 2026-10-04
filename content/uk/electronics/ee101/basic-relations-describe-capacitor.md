---
id: emb-elee-0020
title: "Які основні співвідношення описують конденсатор?"
description: "Які основні співвідношення описують конденсатор?"
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
    applicability: "Походження питання: лекція 35, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-capacitor-calculus
    title: "All About Circuits: Capacitors and Calculus"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/capacitors-and-calculus/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Співвідношення струму, ємності та швидкості зміни напруги; ідеальний capacitor без витоку."
  - source_id: aac-capacitor-fields
    title: "All About Circuits: Electric Fields and Capacitance"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/electric-fields-capacitance/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Накопичення заряду й енергії в electric field та тенденція ідеального capacitor підтримувати напругу."
  - source_id: aac-capacitor-factors
    title: "All About Circuits: Factors Affecting Capacitance"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/factors-affecting-capacitance/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Вплив площі пластин, відстані й permittivity на ємність; формула для геометрії є наближенням."
---

## Short answer

Для лінійного конденсатора `Q = C*V`, `i = C*dV/dt`, а запасена енергія `E = C*V²/2`. Для ідеальних паралельних пластин `C = ε*A/d`; реальні компоненти мають допуски, витік і паразитні параметри.[^aac-capacitor-calculus] [^aac-capacitor-fields]

## Detailed explanation

Конденсатор характеризується ємністю `C`, яка пов’язує заряд на його обкладках із напругою між ними. Для лінійного компонента заряд дорівнює `Q = C*V`: за більшої ємності або напруги на обкладках накопичується більший за модулем заряд. Йдеться про заряд однієї обкладки; на другій є рівний за модулем заряд протилежного знака.[^aac-capacitor-fields]

Струм визначається не самою напругою, а швидкістю її зміни: `i = C*dV/dt` за пасивної домовленості про напрям струму. Якщо напруга постійна, похідна дорівнює нулю, тому ідеальний конденсатор не проводить сталий струм після завершення перехідного процесу. Під час заряджання чи розряджання струм існує; швидша зміна напруги дає більший струм. Реальний компонент має витік, тому його струм за сталого DC не обов’язково точно нульовий.[^aac-capacitor-calculus] [^aac-capacitor-fields]

Енергія зберігається в electric field і для лінійного конденсатора становить `E = C*V²/2`. Формула плоского конденсатора `C = ε*A/d` є моделлю: `A` – площа перекриття пластин, `d` – відстань між ними, `ε` – permittivity діелектрика. Більша площа та вища permittivity збільшують ємність, а більша відстань її зменшує; крайові поля та конструкція реального компонента не враховані.[^aac-capacitor-fields] [^aac-capacitor-factors]

Приклад: якщо `C = 100 µF` і напруга змінюється на `2 V` за `1 ms`, середній струм ідеальної моделі дорівнює `0.2 A` у напрямі заряджання. Це не означає, що конденсатор завжди має такий струм: значення залежить від миттєвого нахилу напруги та зовнішнього кола.

**Типова помилка:** вважати конденсатор «розривом для струму» за будь-яких умов. Сталий ідеальний DC після заряджання не проходить, але змінний сигнал створює струм, а реальний компонент має струм витоку та обмеження за напругою.

## Sources

<!-- generated from frontmatter -->
